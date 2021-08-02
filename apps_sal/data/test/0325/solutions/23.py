# 到達可能な頂点の集合
def reachable_nodeset(start, inc):
    reachable = set()
    reachable.add(start)
    nodes = [start]

    while nodes:
        n = nodes.pop()
        for i in inc[n]:
            if i not in reachable:
                nodes.append(i)
                reachable.add(i)
    return reachable


def bellmanford(num, start, goal, edges):
    cost = [float('inf')] * num
    cost[start] = 0
    # 負の閉路が無ければ更新はV-1回までで終わる
    for _ in range(num):
        updated = False
        for a, b, c in edges:
            # aまでのコスト+辺abのコストがbまでのコストより小さければ更新
            if cost[b] > cost[a] + c:
                cost[b] = cost[a] + c
                updated = True
        if not updated: break
    else:
        # V回目まで更新があったら負の閉路がある
        return -1
    return max(0, -cost[goal])


N, M, P = map(int, input().split())
to = [[] for _ in range(N)]
ot = [[] for _ in range(N)]
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    c = -(c - P)

    to[a].append(b)
    ot[b].append(a)
    edges.append((a, b, c))

reachableFromZero = reachable_nodeset(0, to)
reachableToN = reachable_nodeset(N - 1, ot)
ok = reachableFromZero.intersection(reachableToN)
edges = tuple((a, b, c) for a, b, c in edges if a in ok and b in ok)

print(bellmanford(N, 0, N - 1, edges))
