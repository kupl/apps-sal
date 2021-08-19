n = int(input())


def is_ok(arg):
    return 2 * (n + 1) < arg * (arg + 1)


def meguru_bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok - 1


print(n + 1 - meguru_bisect(1, n + 1))
