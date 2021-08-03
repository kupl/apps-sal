def main():
    n = int(input())
    x_lst = list(map(int, input().split()))
    x_sorted_lst = sorted(x_lst)

    median1 = x_sorted_lst[n // 2 - 1]
    median2 = x_sorted_lst[n // 2]

    if median1 == median2:
        lst = [median1] * n

    else:
        lst = []
        for i in range(n):
            x = x_lst[i]

            if x <= median1:
                lst.append(median2)
            elif median2 <= x:
                lst.append(median1)

    for i in range(n):
        print(lst[i])


def __starting_point():
    main()


__starting_point()
