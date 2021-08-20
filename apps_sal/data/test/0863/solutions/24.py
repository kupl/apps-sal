def main():
    (a, ta) = list(map(int, input().split()))
    (b, tb) = list(map(int, input().split()))
    (h, m) = list(map(int, input().split(':')))
    (res, lo) = (0, h * 60 + m - 300)
    hi = lo + ta
    print(sum((max(lo, t) < min(hi, t + tb) for t in range(0, 1140, b))))


def __starting_point():
    main()


__starting_point()
