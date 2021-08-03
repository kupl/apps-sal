def main():
    n = int(input())
    a_lst = list(map(int, input().split()))
    x = a_lst[0]
    y = sum(a_lst) - x

    minimum = abs(x - y)
    for i in range(1, n - 1):
        a = a_lst[i]
        x += a
        y -= a
        minimum = min(minimum, abs(x - y))

    print(minimum)


def __starting_point():
    main()


__starting_point()
