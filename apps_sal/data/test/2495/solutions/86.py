def main():
    n = int(input())
    A = list(map(int, input().split()))
    s = 0
    c1 = 0
    for (i, a) in enumerate(A):
        s += a
        if i % 2 == 0:
            if s == 0:
                c1 += 1
            elif s < 0:
                c1 += 1 - s
            else:
                continue
            s = 1
        else:
            if s == 0:
                c1 += 1
            elif s > 0:
                c1 += s + 1
            else:
                continue
            s = -1
    s = 0
    c2 = 0
    for (i, a) in enumerate(A):
        s += a
        if i % 2 != 0:
            if s == 0:
                c2 += 1
            elif s < 0:
                c2 += 1 - s
            else:
                continue
            s = 1
        else:
            if s == 0:
                c2 += 1
            elif s > 0:
                c2 += s + 1
            else:
                continue
            s = -1
    print(min(c1, c2))


def __starting_point():
    main()


__starting_point()
