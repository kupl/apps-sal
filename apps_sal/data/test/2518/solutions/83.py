from math import ceil


def f(x, h):
    hp = h
    hp = [hh - b * x for hh in hp]
    count = 0
    for hh in hp:
        if hh <= 0:
            continue
        count += ceil(hh / (a - b))
    return x >= count


(n, a, b) = map(int, input().split())
h = [int(input()) for i in range(n)]
ng = 0
ok = 10 ** 9
while abs(ok - ng) > 1:
    m = (ok + ng) // 2
    if f(m, h):
        ok = m
    else:
        ng = m
print(ok)
