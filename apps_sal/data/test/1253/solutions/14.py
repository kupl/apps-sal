def main():
    n, k = list(map(int, input().split()))
    aa = list(map(int, input().split()))
    lo = sum(a <= 0 for a in aa)
    if lo >= k:
        res = sum(aa[k:]) - sum(aa[:k])
    else:
        res = sum(aa[lo:]) - sum(aa[:lo])
        if aa[lo - 1] and ((k - lo) & 1):
            res -= min(list(map(abs, [_f for _f in aa if _f]))) * 2
    print(res)


def __starting_point():
    main()


__starting_point()
