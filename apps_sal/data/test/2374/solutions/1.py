def main():
    import sys
    input = sys.stdin.readline
    from bisect import bisect_left, bisect_right
    sys.setrecursionlimit(10**9)

    N, M = map(int, input().split())
    AB = []
    for i in [0] * N:
        A, B = map(int, input().split())
        AB.append((A, B))
    AB.sort(key=lambda x: x[0])

    POWER = 1
    x = [0] * (N + 1)
    x[0] = AB[0][POWER]
    for i in range(N - 1):
        x[i + 1] = AB[i][POWER] ^ AB[i + 1][POWER]
    x[N] = AB[N - 1][POWER]

    graph = [[] for _ in [0] * (N + 1)]
    for i in range(1, M + 1):
        L, R = map(int, input().split())
        L = bisect_left(AB, (L, 0))
        R = bisect_right(AB, (R, 1))
        graph[L].append((R, i))
        graph[R].append((L, i))

    ans = []
    POS = 0
    ID = 1

    def dfs(v):
        used[v] = True
        res = x[v]
        for edge in graph[v]:
            if used[edge[POS]]: continue
            r = dfs(edge[POS])
            if r: ans.append(edge[ID])
            res ^= r
        return res

    used = [False] * (N + 1)
    for i in range(N + 1):
        if used[i]: continue
        if dfs(i):
            print(-1)
            return

    print(len(ans))
    ans.sort()
    print(*ans)


main()
