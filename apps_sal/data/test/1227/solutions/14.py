N = input()
K = int(input())
m = len(N)
dp = [[[0] * (K + 1) for _ in range(2)] for _ in range(m + 1)]
dp[0][0][0] = 1  # [i][j][k] i桁目まで決める　N未満で確定でj=1 0でない数がk個

for i in range(1, m + 1):
    l = int(N[i - 1])
    for k in range(K + 1):  # 0でない数の個数 k を変化させていく
        if k == 0:  # すべての数が0ではない場合
            dp[i][0][k] = 0  # i桁目　Nと一致　すべてが0　→　該当なし　0コ
            dp[i][1][k] = 1  # i桁目　N未満　  すべてが0  →　0のみ　  1コ
        else:  # k >= 1
            if l != 0:  # i桁目 1～9
                dp[i][0][k] = dp[i - 1][0][k - 1]
                dp[i][1][k] = dp[i - 1][1][k] + 9 * dp[i - 1][1][k - 1] + dp[i - 1][0][k] + (l - 1) * dp[i - 1][0][k - 1]
            else:  # i桁目 0
                dp[i][0][k] = dp[i - 1][0][k]
                dp[i][1][k] = dp[i - 1][1][k] + 9 * dp[i - 1][1][k - 1]

# print(dp)
print((dp[m][0][K] + dp[m][1][K]))
