n, m = map(int, input().split())

if n <= m:
    print(n)
else:
    ok = 10 ** 100
    ng = 0
    while ok - ng > 1:
        mid = (ok + ng) // 2
        s = n - mid * (mid - 1) // 2 - (m + mid)

        if s <= 0:
            ok = mid
        else:
            ng = mid

    print(ok + m)
