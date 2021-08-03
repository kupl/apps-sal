def main():
    s = input()
    l, i = [], s.find('bear')
    while i >= 0:
        l.append(i)
        i = s.find('bear', i + 4)
    res = []
    for shift in range(min(len(l), 2)):
        res.append(sum((i + 1) * (len(s) - j - 3) for i, j in zip(l, l[shift:])))
    res.append(0)
    res.append(0)
    print(res[0] - res[1])


def __starting_point():
    main()


__starting_point()
