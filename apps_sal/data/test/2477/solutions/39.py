(n, k) = map(int, input().split())
alist = list(map(int, input().split()))


def is_ok(arg):
    cnt = 0
    for i in alist:
        cnt += (i - 1) // arg
    return cnt <= k


def nibun(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(nibun(0, 10 ** 9 + 1))
