def main():
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(((x, i) for (i, x) in enumerate(l)))
    l = sorted(((i, j) for (j, (x, i)) in enumerate(l)))
    l = [j for (x, j) in l]
    index = [0] * n
    for (i, x) in enumerate(l):
        index[x] = i
    res = []
    for (i, x) in enumerate(index):
        y = l[i]
        if i != y:
            res.append((i, x))
            (l[i], l[x]) = (i, y)
            index[y] = x
    print(len(res))
    for a in res:
        print(*a)


def __starting_point():
    main()


__starting_point()
