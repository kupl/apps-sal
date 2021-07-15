def main():
    from bisect import bisect_left
    n, m = list(map(int, input().split()))
    aa = list(map(int, input().split()))
    bb = -10 ** 10, *list(map(int, input().split())), 10 ** 10
    rr = [bb[bisect_left(bb, a)] - a for a in aa]
    bb = [-b for b in reversed(bb)]
    rr.reverse()
    aa.reverse()
    for i, r, a in zip(list(range(n)), rr, aa):
        x = bb[bisect_left(bb, -a)] + a
        if r > x:
            rr[i] = x
    print(max(rr))


def __starting_point():
    main()

__starting_point()
