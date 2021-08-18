
def solve():
    import sys
    import heapq

    MAX_S = 50 * 50
    N, M, S = list(map(int, sys.stdin.readline().split()))
    graph = [[] for _ in range(N)]

    for _ in range(M):
        u, v, a, b = list(map(int, sys.stdin.readline().split()))
        u, v = u - 1, v - 1
        graph[u].append((v, a, b))
        graph[v].append((u, a, b))

    ryogae = []
    for _ in range(N):
        c, d = list(map(int, sys.stdin.readline().split()))
        ryogae.append((c, d))

    dp = [[float("inf") for _ in range(MAX_S + 1)] for __ in range(N)]

    s = min(S, MAX_S)
    que = []
    heapq.heappush(que, (0, 0, s))

    while len(que) != 0:
        t, v, s = heapq.heappop(que)

        c, d = ryogae[v]
        ns = min(s + c, MAX_S)
        if dp[v][ns] > t + d:
            dp[v][ns] = t + d
            heapq.heappush(que, (t + d, v, ns))

        for u, a, b in graph[v]:
            if s - a < 0:
                continue
            if dp[u][s - a] > t + b:
                dp[u][s - a] = t + b
                heapq.heappush(que, (t + b, u, s - a))

    for v in range(1, N):
        ans = float("inf")
        for s in range(MAX_S + 1):
            ans = min(ans, dp[v][s])
        print(ans)


def __starting_point():
    solve()


__starting_point()
