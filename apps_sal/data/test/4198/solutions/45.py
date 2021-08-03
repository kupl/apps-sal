import math

A, B, X = map(int, input().split())

a = 10**9 + 1
b = X


def is_ok(arg):
    return A * arg + B * int(math.log10(arg) + 1) <= b


def bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(bisect(a, 0))
