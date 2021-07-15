from math import *

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def lcm(x,y):
    return x*y//gcd(x,y)
n = int(input())
a = [int(x) for x in input().split()]

mod = 1000000000+7

k = 1
for x in a:
    k = lcm(k,x)

ans = 0

for x in a:
    ans += k//x

print((ans%mod))

