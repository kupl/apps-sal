import math

n, k = map(int, input().split())
a = list(map(int, input().split()))


def is_ok(x, a, k):
    b = 0
    for ai in a:
        b += math.ceil(ai / x)
        b -= 1
    if b <= k:
        return True


def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, a, k):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(0, max(a)))
