def exgcd(i, j):
    if j == 0:
        return 1, 0, i
    u, v, d = exgcd(j, i % j)
    return v, u - v * (i // j), d
ma, ra, mb, rb, L, R = list(map(int, input().split(' ')))
L = max(L, ra, rb)
if L > R:
    print(0)
    return
if ra > rb:
    ma, ra, mb, rb = mb, rb, ma, ra
_, _, md = exgcd(ma, mb)
if md != 1:
    if (rb - ra) % md != 0:
        print(0)
        return
    m = ma * mb // md
    rev, _, _ = exgcd(ma // md, mb // md)
    rev = (rev % (mb // md) + mb // md) % (mb // md)
    r = ma * (rb - ra) // md * rev + ra
    r = (r % m + m) % m
else:
    m = ma * mb
    bv, av, _ = exgcd(ma, mb)
    r = ra * mb * av + rb * ma * bv
    r = (r % m + m) % m
def calc(i):
    return (i - r) // m
print(calc(R) - calc(L - 1))

