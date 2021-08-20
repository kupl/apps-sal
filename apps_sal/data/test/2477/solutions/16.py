import math
(N, K) = map(int, input().split())
l = list(map(int, input().split()))


def f(n):
    A = 0
    for i in l:
        A += math.ceil(i / n) - 1
    return A <= K


def bis(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(bis(0, max(l)))
