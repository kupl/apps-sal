import sys
input = sys.stdin.readline

N, M = map(int, input().split())
St = [list(map(int, input().split())) for _ in range(N)]


dp = [M - i for i in range(M + 1)]

for m in reversed(range(M)):
    covered = False
    for x, s in St:
        if x - s <= m + 1 <= x + s:
            covered = True
            break
        if m < x - s:
            u = x - s - m - 1
            dp[m] = min(dp[m], u + dp[min(M, x + s + u)])
    if covered:
        dp[m] = dp[m + 1]

print(dp[0])
