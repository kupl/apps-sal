import math
N = int(input())
res = 1
for i in range(2, N+1):
    res = res*i//math.gcd(res, i)
print((res+1))

