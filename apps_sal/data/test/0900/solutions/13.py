import numpy as np
MOD = 10 ** 9 + 7

S = [int(x) if x != "?" else -1 for x in input()]
N = len(S)

# 現在考えてる一つ前の桁数で、余りが i になる整数の個数
r = [0]*13

# まず一つ目の値が１の位とする
s = S[0]
if s != -1:
  r[s] = 1
else:
  for i in range(10):
    r[i] = 1

# 桁を進めながら個数をカウント
for i in range(1, N):
    # dp[j]
    # 現在考えている桁(i)を除く、余りが j となる整数の個数
    dp = [0]*26
    # 桁が一つ上がるので、一つ前の余りが 10 倍になる
    for j in range(13):
      dp[j*10%13] += r[j] % MOD
    # アクセスを高速にするため２倍の長さとる (dp[i] == dp[i + 13])
    dp[13:26] = dp[0:13]
    r = [0]*13
    s = S[i]
    if s == -1:
      w = sum(dp[4:14])
      for j in range(13):
        r[j] += w
        w += dp[j+1] -dp[j+4]
    else:
      for j in range(13):
        r[j] += dp[13-s+j]
print(r[5]%MOD)        
