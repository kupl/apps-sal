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
    v = n - i
    print(0 if n - i < a else((v - a + 1) * p[i] * pow(v + 1, M - 2, M) + (v - a) * (p[-1] - p[i]) * pow(v, M - 2, M)) % M)
