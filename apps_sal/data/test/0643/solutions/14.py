for case in range(int(input())):
    (x, y, p, q) = map(int, input().split())
    lo = 0
    hi = 10 ** 10
    while lo < hi:
        mid = lo + (hi - lo) // 2
        (np, nq) = (mid * p, mid * q)
        if nq >= y and np >= x:
            if nq - y >= np - x:
                hi = mid
            else:
                lo = mid + 1
        else:
            lo = mid + 1
    print(lo * q - y if lo != 10 ** 10 else -1)
