import sys
import bisect
M = 998244353
def y(): return map(int, sys.stdin.readline().split())


n, m = y()
d = sorted(y())
p = [0]
for i in d:
    p += [p[-1] + i]
for _ in range(m):
    a, b = y()
    i = bisect.bisect_left(d, b)
    print(0 if n - i < a else((n - i - a + 1) * p[i] * pow(n - i + 1, M - 2, M) + (n - i - a) * (p[-1] - p[i]) * pow(n - i, M - 2, M)) % M)
