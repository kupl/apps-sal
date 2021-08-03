N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
UP = max(A)
UL = UP.bit_length()
KL = K.bit_length()
MAX = max(UL, KL)
INF = float("inf")
# dp[i][j]: 上からi桁目までを決めて、N未満で確定ならj=1、Nと一致しているならばj=0
dp = [[-INF] * 2 for _ in range(MAX + 1)]  # -INFにしておかないとないケースから来てしまう。
dp[0][0] = 0
ZF = True
L = [[0] * 2 for _ in range(MAX)]
for i in range(N):
    for j in range(MAX):
        if A[i] >> j & 1 == 1:
            L[MAX - 1 - j][1] += 1
        else:
            L[MAX - 1 - j][0] += 1

# print(MAX,KL)
# print(L)
for i in range(MAX):
    fac = pow(2, (MAX - 1 - i))
    if K >> (MAX - 1 - i) & 1 == 1:
        ZF = False
    if ZF:  # ここのビットは必ず0．つまり1の個数がかけられる。
        dp[i + 1][0] = dp[i][0] + fac * L[i][1]
        dp[i + 1][1] = 0
    else:
        if K >> (MAX - 1 - i) & 1 == 1:
            kbit = 1
        else:
            kbit = 0
        # print(kbit,i)
        if kbit == 1:  # どちらでも良い
            dp[i + 1][1] = max(dp[i][1] + fac * max(L[i]), dp[i][0] + fac * L[i][1])  # 未満
            dp[i + 1][0] = dp[i][0] + fac * L[i][0]  # 一致, kbitが1なので0の個数
        else:  # 完全一致なら0のみ、それ以外ならどちらも
            dp[i + 1][1] = dp[i][1] + fac * max(L[i])  # 未満
            dp[i + 1][0] = dp[i][0] + fac * L[i][1]  # 一致 kbitが0なので1の個数
# print(dp)
ans = max(dp[MAX])
print(ans)
