import heapq


def main():
    (N, M, S) = map(int, input().split())
    money_max = 50 * N
    S = min(S, money_max)
    dp = [[float('inf')] * (money_max + 1) for _ in range(N)]
    dp[0][S] = 0
    G = [[] for _ in range(N)]
    exchange = [None] * N
    for _ in range(M):
        (u, v, a, b) = map(int, input().split())
        (u, v) = (u - 1, v - 1)
        G[u].append([v, a, b])
        G[v].append([u, a, b])
    for i in range(N):
        (c, d) = map(int, input().split())
        exchange[i] = [c, d]
    q = []
    heapq.heapify(q)
    heapq.heappush(q, [0, 0, S])
    while 0 < len(q):
        (pre_time, idx, s) = heapq.heappop(q)
        if dp[idx][s] < pre_time:
            continue
        ex = min(s + exchange[idx][0], money_max)
        if dp[idx][s] + exchange[idx][1] < dp[idx][ex]:
            dp[idx][ex] = dp[idx][s] + exchange[idx][1]
            heapq.heappush(q, [dp[idx][ex], idx, ex])
        for (to, money, time) in G[idx]:
            if money <= s:
                if dp[idx][s] + time < dp[to][s - money]:
                    dp[to][s - money] = dp[idx][s] + time
                    heapq.heappush(q, [dp[to][s - money], to, s - money])
    for i in range(1, N):
        print(min(dp[i]))


def __starting_point():
    main()


__starting_point()
