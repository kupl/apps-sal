def main():
    n, res = int(input()), []
    l = list(map(int, input().split()))
    for _ in range(int(input())):
        w, h = list(map(int, input().split()))
        m = max(l[0], l[w - 1])
        res.append(m)
        l[0] = m + h
    print('\n'.join(map(str, res)))


def __starting_point():
    main()


__starting_point()
