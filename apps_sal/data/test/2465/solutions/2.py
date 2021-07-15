from math import gcd
n = int(input())
for i in range(n):
    k = int(input())
    u = 180//gcd(180,k)
    if u-u*k//180 <2:
        u*=2
    print(u)
