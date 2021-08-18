n = int(input())
if n == 1 or n == 2:
    print(1)
    return


def is_ok(arg):
    return (1 + arg) * (arg) // 2 <= n + 1


def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


tmp = meguru_bisect(n + 1, 1)
ans = (n - tmp)
print(ans + 1)
