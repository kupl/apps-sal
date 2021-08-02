def main():
    q = int(input())
    d = {}
    for _ in range(q):
        old, new = input().split()
        oldold = d.get(old)
        if oldold:
            del d[old]
            d[new] = oldold
        else:
            d[new] = old
    l = [str(len(d))]
    for k, v in d.items():
        l.append(' '.join((v, k)))
    print('\n'.join(l))


def __starting_point():
    main()


__starting_point()
