n, m = map(int, input().split())
if n <= m:
    print(n)
else:
    init = m
    n = n - m
    lo = 1
    hi = int(1e19)
    poss = 0
    while hi >= lo:
        mid = (hi + lo) // 2
        consumed = mid * (mid + 1) // 2
        if consumed >= n:
            poss = mid
            hi = mid - 1
        else:
            lo = mid + 1
    print (poss + init)
