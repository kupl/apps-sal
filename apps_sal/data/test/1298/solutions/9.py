def main():
    n = input()
    s = input()
    d = {'0': 0, '1': 0}
    for c in s:
        d[c] += 1
    print(len(s) - min(d['0'], d['1']) * 2)


def __starting_point():
    main()


__starting_point()
