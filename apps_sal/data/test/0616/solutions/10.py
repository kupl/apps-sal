import sys
input = sys.stdin.readline


def solve():
    INF = 10 ** 10
    (N, M) = list(map(int, input().split()))
    keys = []
    costs = []
    for _ in range(M):
        (a, b) = list(map(int, input().split()))
        costs.append(a)
        cs = list(map(int, input().split()))
        key = 0
        for c in cs:
            key |= 1 << c - 1
        keys.append(key)
    dp = [INF] * (1 << N)
    dp[0] = 0
    for S in range(1 << N):
        for (key, cost) in zip(keys, costs):
            S2 = S | key
            c2 = dp[S] + cost
            if c2 < dp[S2]:
                dp[S2] = c2
    if dp[-1] == INF:
        print(-1)
    else:
        print(dp[-1])


solve()
