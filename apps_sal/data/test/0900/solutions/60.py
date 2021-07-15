import numpy as np
MOD=10**9+7

S=[int(x) if x != "?" else -1 for x in input()]
N=len(S)

#現在考えてる1つ前の桁数で, 余りがiになる整数の個数
r=[0]*13

#まず1つ目の値が1の位とする
s=S[0]
if s != -1:
  r[s] = 1
else:
  for i in range(10):
    r[i] = 1

#桁を進めながら個数をカウント
for i in range(1,N):
  #dp[j]
  #現在考えている桁(i)を除く, 余りがjとなる整数の個数
  dp = [0]*26
  #桁が1つ上がるので, 1つ前のあまりが10倍になる
  for j in range(13):
    dp[j*10%13] += r[j] % MOD
  #アクセスを高速にするため2倍の長さをとる(dp[i]==di[i+13])
  dp[13:26] = dp[0:13]
  r=[0]*13
  s=S[i]
  if s == -1:
    w=sum(dp[4:14])
    for j in range(13):
      r[j] += w
      w += dp[j+1] -dp[j+4]
  else:
    for j in range(13):
      r[j] += dp[13-s+j]
print(r[5]%MOD)
