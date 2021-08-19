(n, m) = list(map(int, input().split()))
dias = [int(x) for x in input().split()]
prep = [int(x) for x in input().split()]


def es_posible(nu):
    faltan = set(range(1, m + 1))
    porestudiar = 0
    for i in reversed(list(range(min(nu, n)))):
        if dias[i] in faltan:
            faltan.remove(dias[i])
            porestudiar += prep[dias[i] - 1]
        elif porestudiar > 0:
            porestudiar -= 1
    return len(faltan) == 0 and porestudiar == 0


if not es_posible(n):
    print(-1)
else:
    (lo, hi) = (0, n)
    while hi > lo:
        mid = (hi + lo) // 2
        if es_posible(mid):
            hi = mid
        else:
            lo = mid + 1
    print(lo)
