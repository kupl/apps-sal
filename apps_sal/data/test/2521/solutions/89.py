from heapq import heappush, heapreplace


N = int(input())
A = list(map(int, input().split()))

dp = [0] * (N + 1)
q = []
cnt = 0
for i in range(N):
    a = A[i]
    heappush(q, a)
    cnt += a
dp[0] = cnt
for i in range(N, 2 * N):
    a = A[i]
    if a > q[0]:
        cnt += a - heapreplace(q, a)
    dp[i - N + 1] = cnt


dp2 = [0] * (N + 1)
q = []
cnt = 0
for i in range(2 * N, 3 * N):
    a = A[i]
    heappush(q, -a)
    cnt += a
dp2[N] = cnt
for i in range(2 * N - 1, N - 1, -1):
    a = A[i]
    if a < -q[0]:
        cnt += a - (-heapreplace(q, -a))
    dp2[i - N] = cnt

ans = -float('inf')
for i in range(N + 1):
    ans = max(ans, dp[i] - dp2[i])
print(ans)
