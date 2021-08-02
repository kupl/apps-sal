def main():
    n, m = map(int, input().split())
    ab_lst = []
    for i in range(m):
        ab_lst.append(list(map(int, input().split())))

    flag = False
    lst = []
    for i in range(m):
        a = ab_lst[i][0]
        b = ab_lst[i][1]

        if a == 1:
            lst.append(b)
    st = set(lst)

    for i in range(m):
        a = ab_lst[i][0]
        b = ab_lst[i][1]

        if b == n:
            if a in st:
                flag = True
                break

    if flag:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')


def __starting_point():
    main()


__starting_point()
