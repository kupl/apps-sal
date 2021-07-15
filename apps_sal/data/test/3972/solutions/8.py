import sys
MOD = 10**9 + 7
N = int(input())
if N == 1:
  print((1)); return;
if N == 2:
  print((4)); return;

DP = [0 for _ in range(N)]
DP[0] = 1
DP[1] = 1
DP_sum = 2
for i in range(2,N):
  DP[i] =  DP_sum - DP[i-2] # DP[0] + DP[1] + ... + DP[i-1] - DP[i-2]
  DP[i] %= MOD
  DP_sum += DP[i]
  DP_sum %= MOD
#print(DP)

ans = 0
fac = (N-1)**2 % MOD
for i in range(N-1):
  ans += DP[i]*(fac+i+2)
  if i >= N-2:
    ans -= DP[i]
  ans %= MOD
ans += DP[N-1] * N
ans %= MOD
  
print((ans % MOD))

