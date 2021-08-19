def main():
    (x, y, a, b) = map(int, input().split())
    res = [None]
    for i in range(a, x + 1):
        si = str(i)
        for j in range(b, min(y + 1, i)):
            res.append(' '.join((si, str(j))))
    res[0] = str(len(res) - 1)
    print('\n'.join(res))


def __starting_point():
    main()


__starting_point()
