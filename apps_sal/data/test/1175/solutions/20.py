from functools import lru_cache
P = 10**9+7
@lru_cache(maxsize=None)
def subcalc(l, r):
    if l > r: return 0
    if r == 0: return 1
    aa, bb = l.bit_length(), r.bit_length()
    if aa == bb:
        return subcalc(l-(1<<aa-1), r-(1<<bb-1))
    if (r & (r+1) == 0) and (l == 0):
        return pow(3, r.bit_length(), P)
    return (subcalc(l, r-(1<<bb-1)) + subcalc(l, (1<<bb-1)-1) + subcalc(0, r-(1<<bb-1))) % P

@lru_cache(maxsize=None)
def calc(L, R):
    if L > R: return 0
    a = L.bit_length()
    b = R.bit_length()
    if b > a:
        return (calc(L, (1<<b-1)-1) + calc(1<<b-1, R)) % P
    a = 1 << L.bit_length() - 1 if L else 0
    return subcalc(L-a, R-a)

L, R = list(map(int, input().split()))
print((calc(L, R)))

