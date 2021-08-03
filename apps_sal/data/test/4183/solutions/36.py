import math
n = int(input())
t = [int(input()) for i in range(n)]
res = t[0]
for i in range(1, n):
    res = res * t[i] // math.gcd(res, t[i])
print(res)
