def main():
    n = int(input())
    a_lst = list(map(int, input().split()))
    lst = [0, 0]

    a_lst.sort()
    a_lst.reverse()

    length = a_lst[0]
    count = 0
    for i in range(n):
        if a_lst[i] == length:
            count += 1

            if count == 2:
                lst.append(a_lst[i])
                count = 0

            if len(lst) == 4:
                break

        else:
            count = 1
            length = a_lst[i]

    area = lst[-1] * lst[-2]
    print(area)


def __starting_point():
    main()
__starting_point()
