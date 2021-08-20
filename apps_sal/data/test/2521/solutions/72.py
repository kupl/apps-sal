from heapq import heapreplace, heapify
N = int(input())
A = list(map(int, input().split()))
dp = [0] * (N + 1)
q = A[:N]
heapify(q)
dp[0] = sum(q)
for i in range(N, 2 * N):
    a = A[i]
    if a > q[0]:
        dp[i - N + 1] += a - heapreplace(q, a)
    dp[i - N + 1] += dp[i - N]
dp2 = [0] * (N + 1)
q = [-A[i] for i in range(2 * N, 3 * N)]
heapify(q)
dp2[N] = -sum(q)
for i in range(2 * N - 1, N - 1, -1):
    a = A[i]
    if a < -q[0]:
        dp2[i - N] += a - -heapreplace(q, -a)
    dp2[i - N] += dp2[i - N + 1]
ans = -float('inf')
for i in range(N + 1):
    ans = max(ans, dp[i] - dp2[i])
print(ans)
