import math
n,m = map(int,input().split())
mod = 10**9+7
fact_n = math.factorial(n) % mod
fact_m = math.factorial(m) % mod

if abs(n-m) >= 2:
  print(0)
elif n == m:
  print((fact_n * fact_m * 2) % mod)
else:
  print((fact_n * fact_m) % mod)
