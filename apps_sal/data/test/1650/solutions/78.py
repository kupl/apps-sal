# E - Sum Equals Xor
# https://atcoder.jp/contests/abc129/tasks/abc129_e

MOD = 10 ** 9 + 7

L = input()
N = len(L)

# dp[i][j]= 上から i 桁目までを決めて、その桁までが (a, b) = [(0,0),(0,1),(1,0)] の3通りから選ばれていて、
# a+b が L より小さいことが確定している(j=1)/していない(j=0)ような選び方の個数
dp = [[0] * 2 for _ in range(N + 1)]
dp[0][0] = 1

for i, s in enumerate(L):
  dp[i + 1][0] = dp[i][0] * 2 if int(s) else dp[i][0] 
  dp[i + 1][1] = dp[i][0] if int(s) else 0
  dp[i + 1][1] += dp[i][1] * 3
  dp[i + 1][0] %= MOD
  dp[i + 1][1] %= MOD

print(sum(dp[N]) % MOD)
