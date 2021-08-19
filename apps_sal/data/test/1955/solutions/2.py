def check(m, mid, aa, dd, edays):
    (avail, ee) = ([True] * (m + 1), [])
    for i in range(mid, -1, -1):
        day = edays[i]
        exam = dd[day]
        if avail[exam]:
            avail[exam] = False
            ee.append(day)
            if len(ee) == m:
                break
    else:
        return False
    (pool, prev) = (0, -1)
    for day in reversed(ee):
        pool += day - prev - aa[dd[day]]
        if pool < 0:
            return False
        prev = day
    return True


def main():
    (n, m) = list(map(int, input().split()))
    dd = list(map(int, input().split()))
    edays = [i for (i, e) in enumerate(dd) if e]
    aa = [0, *(int(s) + 1 for s in input().split())]
    (lo, hi) = (0, len(edays))
    try:
        while lo < hi:
            mid = (lo + hi) // 2
            if check(m, mid, aa, dd, edays):
                hi = mid
            else:
                lo = mid + 1
        print(edays[lo] + 1)
    except IndexError:
        print(-1)


def __starting_point():
    main()


__starting_point()
