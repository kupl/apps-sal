import bisect

N = int(input())
A = [int(input()) for _ in range(N)]
dp = [-1] * N
dp[N-1] = A[0]

ans = 0
for i in range(1, N):
    target_index = bisect.bisect_left(dp, A[i])
    dp[target_index-1] = A[i]

print(N - dp.count(-1))
