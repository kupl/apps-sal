

from math import gcd
N = int(input())
a = list(map(int, input().split()))

ans = a[0]


for aval in a:
    ans = gcd(ans, aval)

print(ans)
