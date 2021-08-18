import sys
input = sys.stdin.readline


N, M = map(int, input().split())
A = list(map(int, input().split()))

num = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

dp = [-float("inf")] * (N + 1)
dp[0] = 0
for a in A:
    if num[a] <= N:
        dp[num[a]] = 1

for i in range(1, N + 1):
    for a in A:
        if i - num[a] >= 0:
            dp[i] = max(dp[i], dp[i - num[a]] + 1)

A.sort(reverse=True)
ans = ""
for i in range(dp[N]):
    for a in A:
        if N - num[a] >= 0 and dp[N - num[a]] == dp[N] - 1:
            ans += str(a)
            N -= num[a]
            break

print(ans)
