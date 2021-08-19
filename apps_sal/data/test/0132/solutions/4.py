def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    res = 100 ** 10
    for l in range(n):
        for r in range(l, n):
            s1 = sum(a[l:r])
            res = min(res, abs(s1 - (s - s1)))
    print(res)


def __starting_point():
    main()


__starting_point()
