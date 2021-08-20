import sys
import bisect
input = sys.stdin.readline
MOD = 998244353


def frac(a, b):
    return a * pow(b, MOD - 2, MOD) % MOD


(n, m) = map(int, input().split())
d = sorted(list(map(int, input().split())))
tot = sum(d)
pref = [0]
for v in d:
    pref.append(pref[-1] + v)
out = [0] * m
for _ in range(m):
    (a, b) = map(int, input().split())
    ind = bisect.bisect_left(d, b)
    sum_before = pref[ind]
    rest = tot - pref[ind]
    if a <= n - ind:
        out[_] += sum_before * frac(n - ind - a + 1, n - ind + 1)
        out[_] += rest * frac(n - ind - a, n - ind)
        out[_] %= MOD
print('\n'.join(map(str, out)))
