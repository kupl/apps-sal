def main():
    n, l, ones = int(input()), [], []
    for i in range(n):
        degree, s = list(map(int, input().split()))
        l.append((degree, s))
        if degree == 1:
            ones.append(i)
    res = []
    while ones:
        i = ones.pop()
        degree, j = l[i]
        if degree == 1:
            res.append(' '.join((str(i), str(j))))
            degree, s = l[j]
            s ^= i
            degree -= 1
            l[j] = degree, s
            if degree == 1:
                ones.append(j)
    print(len(res))
    print('\n'.join(res))


def __starting_point():
    main()


__starting_point()
