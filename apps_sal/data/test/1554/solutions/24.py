def main():
    n, res = int(input()), []
    s, i, fmt = set(), 1, "{:n} {:n}".format
    for j, a in enumerate(input().split(), 1):
        if a in s:
            s = set()
            res.append(fmt(i, j))
            i = j + 1
        else:
            s.add(a)
    if res:
        print(len(res))
        res[-1] = res[-1].split()[0] + ' ' + str(n)
        print('\n'.join(res))
    else:
        print(-1)


def __starting_point():
    main()

__starting_point()
