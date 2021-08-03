a, b, x = map(int, input().split())


def is_ok(arg):
    return a * arg + b * len(str(arg)) <= x


def meguru_bisect(ok, ng):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(0, 10**9 + 1))
