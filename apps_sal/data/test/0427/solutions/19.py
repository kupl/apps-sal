def main():
    cnt1, cnt2, x, y = list(map(int, input().split()))
    lo = cnt3 = cnt1 + cnt2
    hi, z = 10 ** 10, x * y
    while lo < hi:
        v = (lo + hi) // 2
        if (v - v // x < cnt1) or (v - v // y < cnt2) or (v - v // z < cnt3):
            lo = v + 1
        else:
            hi = v
    print(lo)


def __starting_point():
    main()


__starting_point()
