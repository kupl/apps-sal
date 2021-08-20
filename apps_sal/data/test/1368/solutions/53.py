import math
from collections import Counter
(n, a, b) = map(int, input().split())
v = list(map(int, input().split()))
v.sort()
max_mean = sum(v[-a:]) / a
print(max_mean)
cva = Counter(v[-a:])
cv = Counter(v)


def ncr(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


if v[-a] == max_mean:
    ans = 0
    for k in range(a, min(b, cv[v[-a]]) + 1):
        ans += ncr(cv[v[-a]], k)
    print(ans)
else:
    k0 = cva[v[-a]]
    k1 = cv[v[-a]]
    ans = ncr(k1, k0)
    print(ans)
