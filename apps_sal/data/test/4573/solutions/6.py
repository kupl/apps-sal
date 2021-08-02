def main():
    n = int(input())
    x = [int(xn) for xn in input().split()]
    x_sorted = sorted(x)
    idx_median = n // 2
    median_low = x_sorted[idx_median - 1]
    median_high = x_sorted[idx_median]
    for xn in x:
        print((median_high if xn <= median_low else median_low))


def __starting_point():
    main()


__starting_point()
