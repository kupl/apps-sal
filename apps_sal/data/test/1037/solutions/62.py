n = int(input())
a = list(map(int, input().split()))
a = list(zip(list(range(n)), a))  # [index,a]の配列
a.sort(key=lambda x: x[1])  # aの昇順で並べる
dp = [[0 for i in range(n + 1)]for j in range(n + 1)]  # dp[x][y]:=左にx、右にy人並べたときの最大値
ans = 0
for k in range(n):  # k人目まで終了、k+1人目に対して
    i, ai = a.pop()  # aの大きいものから取り出す
    dp[k + 1][0] = dp[k][0] + ai * (i - k)
    dp[0][k + 1] = dp[0][k] + ai * (n - k - 1 - i)
    for l in range(k):  # 右にl+1人並べたとき
        dp[k - l][l + 1] = max(dp[k - l - 1][l + 1] + ai * (i - k + l + 1), dp[k - l][l] + ai * (n - l - 1 - i))
for k in range(n + 1):
    ans = max(ans, dp[k][n - k])

print(ans)
