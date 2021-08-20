def main():
    m = ((1, 1, 1, 0, 1, 1, 1), (0, 0, 1, 0, 0, 1, 0), (1, 0, 1, 1, 1, 0, 1), (1, 0, 1, 1, 0, 1, 1), (0, 1, 1, 1, 0, 1, 0), (1, 1, 0, 1, 0, 1, 1), (1, 1, 0, 1, 1, 1, 1), (1, 0, 1, 0, 0, 1, 0), (1, 1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 0, 1, 1))
    (u, v) = list(map(int, input()))
    tot = 0
    for i in range(100):
        (x, y) = divmod(i, 10)
        diff = 0
        for (aa, bb) in ((u, x), (v, y)):
            for (a, b) in zip(m[aa], m[bb]):
                if a > b:
                    diff = 100
                    break
                diff += a < b
        if diff < 100:
            tot += 1
    print(tot)


def __starting_point():
    main()


__starting_point()
