N, M, P = list(map(int, input().split()))
abc = []
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = list(map(int, input().split()))
    # 向かってくる矢印
    edge[b - 1].append(a - 1)
    abc.append((a - 1, b - 1, P - c))


def dfs(edge, goal):
    #goal = n-1
    used = {goal}
    q = [goal]
    while q:
        v = q.pop()
        for w in edge[v]:
            if w in used:
                continue
            used.add(w)
            q.append(w)

    return used


def bellman_ford(v, s, g, e):
    '''
    v: vertex(頂点)
    s: start.  in this case,0
    g: goal. in this case,n-1
    e: (edge_start,egde_goal,score)
    今回はp-cの最小値を求めていく.
    '''
    inf = 10**10
    # cost : d[V]
    d = [inf] * v
    # 開始点のコストを0とする
    d[s] = 0
    for _ in range(v):
        flag = False
        for a, b, c in e:
            # a -> b の向きを考える
            if d[a] == inf:
                continue
            cost = d[a] + c
            if cost < d[b]:
                d[b] = cost
                flag = True
        if not flag:
            break
    if flag:
        return -1
    return max(-d[g], 0)


vertex = dfs(edge, N - 1)
abc_ = [(a, b, c) for a, b, c in abc if a in vertex and b in vertex]
print((bellman_ford(N, 0, N - 1, abc_)))
