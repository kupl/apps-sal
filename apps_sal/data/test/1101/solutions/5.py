def main():
    from bisect import bisect
    (n, k) = list(map(int, input().split()))
    l = [i for (i, c) in enumerate(input()) if c == '0']
    l.append(n * 3)
    for (i, j) in enumerate(range(k, len(l) - 1)):
        (lo, hi) = (l[i], l[j])
        m = bisect(l, (lo + hi) // 2)
        mid = l[m]
        (a, b) = (mid - lo, hi - mid)
        if a < b:
            a = b
        mid = l[m - 1]
        (b, c) = (mid - lo, hi - mid)
        if b < c:
            b = c
        if a > b:
            a = b
        if n > a:
            n = a
    print(n)


def __starting_point():
    main()


__starting_point()
