def main():
    n = int(input())
    a_lst1 = list(map(int, input().split()))
    a_lst2 = list(map(int, input().split()))
    candies_lst = []

    tmp = 1
    while tmp <= n:
        a1_tmp = a_lst1[:tmp]
        a2_tmp = a_lst2[tmp-1:]
        a1 = sum(a1_tmp)
        a2 = sum(a2_tmp)

        tmp += 1
        candies = a1 + a2
        candies_lst.append(candies)

    maximum = max(candies_lst)
    print(maximum)


def __starting_point():
    main()
__starting_point()
