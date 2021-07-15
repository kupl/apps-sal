from math import *
T = int(input())
for i in range(T):
    a = int(input())
    g = gcd(180, a)
    n = 180 // g
    u = (360 + 180 - a-1) // (180 - a)
    n = (u+n-1)//n * n
    print(n)

