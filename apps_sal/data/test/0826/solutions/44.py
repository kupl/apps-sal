def is_ok(k):
    return k * (1 + k) // 2 <= n + 1


def meguru_bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


n = int(input())
ans = meguru_bisect(n + 1, 0)
print(n + 1 - ans)
