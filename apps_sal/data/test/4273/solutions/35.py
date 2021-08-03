def idx_cmb(n, r):
    import itertools
    lst1 = [i for i in range(0, n)]
    lst = list(itertools.combinations(lst1, r))
    return lst


def main():
    n = int(input())
    s_lst = [str(input()) for _ in range(n)]

    march = [0] * 5
    for i in range(n):
        s = s_lst[i]
        if s[0] == 'M':
            march[0] += 1
        elif s[0] == 'A':
            march[1] += 1
        elif s[0] == 'R':
            march[2] += 1
        elif s[0] == 'C':
            march[3] += 1
        elif s[0] == 'H':
            march[4] += 1

    idx_lst = idx_cmb(5, 3)
    x = 0
    for i in range(len(idx_lst)):
        idx1 = idx_lst[i][0]
        idx2 = idx_lst[i][1]
        idx3 = idx_lst[i][2]
        number1 = march[idx1]
        number2 = march[idx2]
        number3 = march[idx3]
        x += number1 * number2 * number3

    print(x)


def __starting_point():
    main()


__starting_point()
