from math import ceil
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()


def is_ok(l):
    cnt = 0
    for i in range(n):
        cnt += ceil(a[i] / l) - 1
    return True if cnt <= k else False


def meguru_bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(0, a[-1] + 1))
