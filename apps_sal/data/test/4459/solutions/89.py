def main():
    n = int(input())
    a_lst = list(map(int, input().split()))
    a_lst.sort()
    a_set_lst = list(set(a_lst))
    a_set_lst.sort()

    count_lst = []
    count = 1
    if n == 1:
        count_lst.append(count)
    else:
        for i in range(n - 1):
            a1 = a_lst[i]
            a2 = a_lst[i + 1]

            if a1 == a2:
                count += 1
                if i == n - 2:
                    count_lst.append(count)
            else:
                count_lst.append(count)
                count = 1
        if a_lst[-1] != a_lst[-2]:
            count_lst.append(count)

    minimum = 0
    for i in range(len(a_set_lst)):
        number = a_set_lst[i]
        count = count_lst[i]

        if count < number:
            minimum += count
        else:
            minimum += count - number

    print(minimum)


def __starting_point():
    main()


__starting_point()
