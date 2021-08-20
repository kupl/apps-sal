import sys
sys.setrecursionlimit(1000000000)


def ii():
    return int(input())


def miis():
    return map(int, input().split())


def lmiis():
    return list(miis())


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
    for _ in range(num):
        updated = False
        for (a, b, c) in edges:
            if cost[b] > cost[a] + c:
                cost[b] = cost[a] + c
                updated = True
        if not updated:
            break
    else:
        return -1
    return max(0, -cost[goal])


def solve():
    (N, M, P) = miis()
    to = [[] for _ in range(N)]
    ot = [[] for _ in range(N)]
    edges = []
    for _ in range(M):
        (a, b, c) = miis()
        a -= 1
        b -= 1
        c = -(c - P)
        to[a].append(b)
        ot[b].append(a)
        edges.append((a, b, c))
    reachableFromZero = reachable_nodeset(0, to)
    reachableToN = reachable_nodeset(N - 1, ot)
    ok = reachableFromZero.intersection(reachableToN)
    edges = tuple(((a, b, c) for (a, b, c) in edges if a in ok and b in ok))
    print(bellmanford(N, 0, N - 1, edges))


def __starting_point():
    solve()


__starting_point()
