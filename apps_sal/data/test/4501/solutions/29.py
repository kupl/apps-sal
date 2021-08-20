import numpy as np
(n, a) = map(int, input().split())
x = list(map(int, input().split()))
'\n平均がa <=> 集合をlとして, len(l)a = sum(l)\ndp[i][j][k] := i番目までのカードを選んだとき, 選んだ枚数がkでの総和がちょうどjになる場合の数.\nこれだとメモリが足りないので, iを省略する.\n'
sumx = sum(x)
dp = np.zeros((n, sumx + 1), dtype=np.int64)
for i in range(n):
    for j in range(i)[::-1]:
        dp[j + 1][x[i]:] += dp[j][:-x[i]]
    dp[0][x[i]] += 1
ans = 0
for i in range(n):
    if (i + 1) * a <= sumx:
        ans += dp[i][(i + 1) * a]
print(ans)
