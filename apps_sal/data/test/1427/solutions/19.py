from math import gcd
mod = 1000000007
n = int(input())
a = list(map(int, input().split()))
d = 1
res = 0
for v in a:
    d *= v // gcd(v, d)
for v in a:
    res += d // v
print(res % mod)
