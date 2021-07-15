L = input()

N = len(L)
mod = int(1e9 + 7)

# 桁DP
# a+b <= N 確定
dp1 = [0] * N
# a+b <= N 未確定
dp2 = [0] * N

# L[0] == 1なので、初期値が決まる（はず）
dp1[0] = 1 # (A0,B0) = (0,0)
dp2[0] = 2 # (A0,B0) = (0,1), (1,0)

for i in range(1,N):
  dp1[i] += dp1[i-1] * 3 # (1,1)以外の3パターン
  dp1[i] %= mod
  if L[i] == '1':
    dp1[i] += dp2[i-1] # (0,0)
    dp2[i] += dp2[i-1] * 2 # (1,0),(0,1)
  else:
    # L[i] == '0'
    dp2[i] += dp2[i-1] # (0,0)
  dp1[i] %= mod
  dp2[i] %= mod
  
print((dp1[N-1] + dp2[N-1]) % mod)
