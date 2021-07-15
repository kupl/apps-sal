import math

n, m, k = [int(x) for x in input().split()]
if k == 0:
    ar = m
else:
    a = m * (math.factorial(n-1) // (math.factorial(k) * math.factorial(n-1-k))) * ((m-1)**k)
    ar = a % 998244353
print(ar)

