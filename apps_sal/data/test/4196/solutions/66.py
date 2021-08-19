from math import gcd
from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))
l = list(accumulate(a, lambda x, y: gcd(x, y)))
r = list(accumulate(a[::-1], lambda x, y: gcd(x, y)))[::-1]
ans = max(r[1], l[-2])
for i in range(1, n - 1):
    ans = max(ans, gcd(l[i - 1], r[i + 1]))
print(ans)
