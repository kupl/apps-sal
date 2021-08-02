from functools import lru_cache
import sys
sys.setrecursionlimit(1000000)
P = 10**9 + 7


@lru_cache(maxsize=None)
def subcalc(l, r):
    if l < 0 or r < 0:
        print("ERROR")
        print("l, r =", l, r)
        print(1 // 0)
    if l > r: return 0
    if r == 0: return 1
    aa, bb = l.bit_length(), r.bit_length()
    if aa == bb:
        return subcalc(l - (1 << aa - 1), r - (1 << bb - 1))
    if (r & (r + 1) == 0) and (l == 0):
        return pow(3, r.bit_length(), P)
    t = (subcalc(l, r - (1 << bb - 1)) + subcalc(l, (1 << bb - 1) - 1) + subcalc(0, r - (1 << bb - 1))) % P
    # print("subcalc", l, r, t)
    return t


@lru_cache(maxsize=None)
def calc(L, R):
    if L < 0 or R < 0:
        print("ERROR")
        print("l, r =", l, r)
        print(1 // 0)
    if L > R: return 0
    a = L.bit_length()
    b = R.bit_length()
    if b > a:
        t = (calc(L, (1 << b - 1) - 1) + calc(1 << b - 1, R)) % P
        # print("calc", L, R, t)
        return t

    a = 1 << L.bit_length() - 1 if L else 0
    t = subcalc(L - a, R - a)
    # print("calc", L, R, t)
    return t


L, R = map(int, input().split())
print(calc(L, R))
