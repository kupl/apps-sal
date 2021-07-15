n = int(input())

from math import gcd
res = 1
for i in range(2,n+1):
    res = res*i//gcd(res,i)

print(res+1)
