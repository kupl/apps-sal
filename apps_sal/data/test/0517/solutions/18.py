def main():
    (n, d, h) = list(map(int, input().split()))
    if h * 2 < d or d < 2 < n or h > d:
        print(-1)
        return
    (res, f) = ([], ' '.join)
    for e in ((2, h + 2), (h + 2, d + 2)):
        a = '1'
        for b in map(str, list(range(*e))):
            res.append(f((a, b)))
            a = b
    a = '1 %d' if h < d else '2 %d'
    res.extend((a % i for i in range(d + 2, n + 1)))
    print('\n'.join(res))


def __starting_point():
    main()


__starting_point()
