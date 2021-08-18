N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
UP = max(A)
UL = UP.bit_length()
KL = K.bit_length()
MAX = max(UL, KL)
INF = float("inf")
dp = [[-INF] * 2 for _ in range(MAX + 1)]
dp[0][0] = 0
ZF = True
L = [[0] * 2 for _ in range(MAX)]
for i in range(N):
    for j in range(MAX):
        if A[i] >> j & 1 == 1:
            L[MAX - 1 - j][1] += 1
        else:
            L[MAX - 1 - j][0] += 1

for i in range(MAX):
    fac = pow(2, (MAX - 1 - i))
    if K >> (MAX - 1 - i) & 1 == 1:
        ZF = False
    if ZF:
        dp[i + 1][0] = dp[i][0] + fac * L[i][1]
        dp[i + 1][1] = 0
    else:
        if K >> (MAX - 1 - i) & 1 == 1:
            kbit = 1
        else:
            kbit = 0
        if kbit == 1:
            dp[i + 1][1] = max(dp[i][1] + fac * max(L[i]), dp[i][0] + fac * L[i][1])
            dp[i + 1][0] = dp[i][0] + fac * L[i][0]
        else:
            dp[i + 1][1] = dp[i][1] + fac * max(L[i])
            dp[i + 1][0] = dp[i][0] + fac * L[i][1]
ans = max(dp[MAX])
print(ans)
