import sys
import bisect
input = sys.stdin.readline
MOD = 998244353
def f(a, b): return a * pow(b, MOD - 2, MOD)


n, m = map(int, input().split())
d = sorted(map(int, input().split()))
pref = [0]
for v in d:
    pref.append(pref[-1] + v)
out = [0] * m
for _ in range(m):
    a, b = map(int, input().split())
    i = bisect.bisect_left(d, b)
    if a <= n - i:
        out[_] = (pref[i] * f(n - i - a + 1, n - i + 1) + (pref[-1] - pref[i]) * f(n - i - a, n - i)) % MOD
print('\n'.join(map(str, out)))
