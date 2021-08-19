def main():
    n = int(input())
    l = [j - i if c == '<' else j + i for (c, i, j) in zip(input(), list(map(int, input().split())), list(range(n)))]
    (v, i) = ([True] * n, 0)
    while 0 <= i < n:
        if v[i]:
            v[i] = False
        else:
            print('INFINITE')
            return
        i = l[i]
    print('FINITE')


def __starting_point():
    main()


__starting_point()
