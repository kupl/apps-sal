def main():
    n = int(input())
    ab_lst = [list(map(int, input().split())) for _ in range(n)]

    ba_lst = [0] * n
    for i in range(n):
        a = ab_lst[i][0]
        b = ab_lst[i][1]
        ba = [b, a]
        ba_lst[i] = ba
    ba_lst.sort()

    lst = []
    b = ba_lst[0][0]
    a = ba_lst[0][1]
    for i in range(n):
        b_tmp = ba_lst[i][0]
        a_tmp = ba_lst[i][1]

        if b == b_tmp:
            if i != 0:
                a += a_tmp
            if i == n - 1:
                lst.append([b, a])

        else:
            lst.append([b, a])
            b = b_tmp
            a = a_tmp

    if len(lst) > 1:
        if ba_lst[-1][0] != ba_lst[-2][0]:
            lst.append([ba_lst[-1][0], ba_lst[-1][1]])


    accumulate = 0
    flag = True
    for i in range(len(lst)):
        accumulate += lst[i][1]
        if accumulate > lst[i][0]:
            flag = False
            break

    if flag:
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()
__starting_point()
