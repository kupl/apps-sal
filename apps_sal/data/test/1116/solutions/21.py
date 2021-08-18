
from fractions import gcd
n = int(input())
for i in range(n):
    r, b, k = list(map(int, input().split()))
    _gcd = gcd(r, b)
    mn = min(r, b) / _gcd
    mx = max(r, b) / _gcd
    if (mx - 1) > mn * (k - 1):
        print("REBEL")
    else:
        print("OBEY")
