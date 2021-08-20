def even(x):
    flag1 = False
    if x % 2 == 0:
        flag1 = True
    return flag1


def multiple_of_4(x):
    flag2 = False
    if x % 2 == 0:
        x //= 2
        if x % 2 == 0:
            flag2 = True
    return flag2


def main():
    n = int(input())
    a_lst = list(map(int, input().split()))
    flag = False
    multiple_of_4_count = 0
    for i in range(n):
        if multiple_of_4(a_lst[i]):
            multiple_of_4_count += 1
    if multiple_of_4_count >= n // 2:
        flag = True
    else:
        even_count = 0
        for i in range(n):
            if even(a_lst[i]):
                even_count += 1
        tmp = n - 2 * multiple_of_4_count
        even_count -= multiple_of_4_count
        if even_count >= tmp:
            flag = True
    if flag:
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()


__starting_point()
