import sys
import math

n = int(input())
gcd = 0
a = {}
b = {}

for i in range(n):
    a[i], b[i] = list(map(int, input().split()))
    gcd = math.gcd(gcd, a[i] * b[i])

for i in range(n):
    ret = math.gcd(gcd, a[i])
    if ret > 1:
        gcd = ret
    else:
        gcd = math.gcd(gcd, b[i])
    if gcd == 1:
        break;
if gcd == 1:
    print(-1)
else:
    print(gcd)
