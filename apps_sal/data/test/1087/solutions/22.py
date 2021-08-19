(N, K) = map(int, input().split())
A = list(map(int, input().split()))
dp = [0] * 41
bp = [0] * 41
for i in range(N):
    o = len(bin(A[i]))
    for j in range(o - 2):
        if A[i] >> j & 1 == 1:
            dp[j] += 1
ans = 0
count = 0
for i in range(len(dp) - 1, -1, -1):
    bp[i] = N - dp[i]
    if dp[i] < bp[i] and count + pow(2, i) <= K:
        count += pow(2, i)
ans = 0
for i in range(N):
    ans += count ^ A[i]
print(ans)
