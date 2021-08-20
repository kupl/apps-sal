def main():
    (n, m) = map(int, input().split())
    ch = [True] * (n + 1)
    for i in range(m):
        (a, b) = map(int, input().split())
        (a, b) = (a - 1, b - 1)
        ch[a] = ch[b] = False
    cen = ch.index(True) + 1
    print(n - 1)
    for i in range(1, n + 1):
        if i == cen:
            continue
        print(cen, i)


def __starting_point():
    main()


__starting_point()
