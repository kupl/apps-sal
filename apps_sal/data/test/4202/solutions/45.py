def main():
    (l, r) = list(map(int, input().split()))
    mi = 2019
    c = 0
    for i in range(l, r):
        a = i * i % 2019
        for _ in range(min(r - l - c, 2019)):
            a = (a + i) % 2019
            if a < mi:
                mi = a
                if a == 0:
                    print(0)
                    return
        c += 1
    print(mi)


def __starting_point():
    main()


__starting_point()
