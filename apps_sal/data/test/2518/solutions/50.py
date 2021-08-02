from math import ceil


def f(x, hp):
    hp = [hh - (b * x) for hh in hp]
    c = 0
    for p in hp:
        if p <= 0: continue
        c += ceil(p / (a - b))
    return c <= x


n, a, b = list(map(int, input().split()))
h = [int(input()) for i in range(n)]
ng = 0
ok = 10**9
while ok - ng > 1:
    mid = (ok + ng) // 2
    if f(mid, h):
        ok = mid
    else:
        ng = mid
print(ok)
