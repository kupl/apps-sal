def main():
    s = str(input())
    q = int(input())
    lst = [list(map(str, input().split())) for _ in range(q)]
    switch = 0

    str_lst = [s]
    front_lst = []
    for i in range(q):

        if lst[i][0] == '1':
            switch = 1 - switch

        else:
            f = lst[i][1]
            c = lst[i][2]

            if f == '1':

                if switch == 0:
                    front_lst.append(c)

                else:
                    str_lst.append(c)

            else:

                if switch == 0:
                    str_lst.append(c)

                else:
                    front_lst.append(c)

    front = ''.join(front_lst)
    front = front[::-1]
    after = ''.join(str_lst)
    answer = front + after

    if switch == 1:
        answer = answer[::-1]

    print(answer)


def __starting_point():
    main()


__starting_point()
