def is_ok(x):
    cnt = 0
    for a in A:
        cnt += -(-a // x) - 1
    if cnt <= k:
        return True
    return False


def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

print((meguru_bisect(0, 10**9 + 1)))
