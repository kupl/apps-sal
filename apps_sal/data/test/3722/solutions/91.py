import sys
MOD = 10**9 + 7
N = int(input())
if N == 2:
  print((1))
  return
  
c = [input() for _ in range(4)]
s = "".join(c)

DP = [0 for i in range(N+1)] #間を開けて選ぶ場合の数(i番目を選ぶ場合)
DP[0] = 1
DP[1] = 1
DP_sum = 2
for i in range(2,N-2):
  DP[i] += DP_sum - DP[i-1]
  DP_sum += DP[i]
  
  
if s == "AAAA" or s == "BBBB" or s == "AABA" or s == "BBAB":
  print((1))
elif s == "AAAB" or s == "ABBB" or s == "ABAB" or s == "AABB":
  print((1))
elif s == "ABAA" or s == "BABB" or s == "BABA" or s == "BBAA":
  print((2**(N-3) % MOD))
elif s == "ABBA" or s == "BAAB" or s == "BAAA" or s == "BBBA":
  if N == 3:
    print((1))
    return
  print((DP_sum % MOD))
  

