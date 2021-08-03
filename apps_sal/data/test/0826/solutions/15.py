def solve():
    N = int(input())

    ok = 1
    ng = N + 1

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if mid * (mid + 1) // 2 <= N + 1:
            ok = mid
        else:
            ng = mid

    print((N - ok + 1))


def __starting_point():
    solve()


__starting_point()
