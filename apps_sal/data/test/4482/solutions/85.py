def main():
    n = int(input())
    a_lst = list(map(int, input().split()))
    minimum = min(a_lst)
    maximum = max(a_lst)

    cost = 10 ** 9
    for i in range(maximum - minimum + 1):
        tmp_cost = 0
        std = minimum + i
        for j in range(n):
            a = a_lst[j]
            tmp_cost += (a - std) ** 2
        cost = min(tmp_cost, cost)

    print(cost)


def __starting_point():
    main()
__starting_point()
