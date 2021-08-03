def main():
    from bisect import bisect_left
    input()
    aa = list(map(int, input().split()))
    bb = -10 ** 10, *list(map(int, input().split())), 10 ** 10
    for i, a in enumerate(aa):
        j = bisect_left(bb, a)
        u, v = bb[j] - a, a - bb[j - 1]
        aa[i] = u if u < v else v
    print(max(aa))


def __starting_point():
    main()


__starting_point()
