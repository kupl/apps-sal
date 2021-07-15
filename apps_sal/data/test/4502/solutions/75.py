def main():
    n = int(input())
    a_lst = list(map(int, input().split()))
    lst1 = []
    lst2 = []

    if n % 2 == 0:
        for i in range(n // 2):
            lst1.append(a_lst[-1 - i * 2])
        for i in range(n // 2):
            lst2.append(a_lst[i * 2])

    else:
        for i in range(n // 2):
            lst1.append(a_lst[-1 - i * 2])
        lst2.append(a_lst[0])
        for i in range(n // 2):
            lst2.append(a_lst[1 + i * 2])

    lst = lst1 + lst2
    ans = ''
    for i in range(n - 1):
        ans += '{} '.format(lst[i])
    ans += '{}'.format(lst[-1])
    print(ans)


def __starting_point():
    main()
__starting_point()
