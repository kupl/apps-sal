import math


def combination(n, r):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def count_list(lst):
    count_lst = [0] * (max(lst) + 1)
    for i in lst:
        count_lst[i] += 1
    return count_lst


def main():
    n = int(input())
    a_lst = list(map(int, input().split()))
    lst1 = count_list(a_lst)
    lst2 = [0] * len(lst1)
    for i in range(len(lst1)):
        lst2[i] = combination(lst1[i], 2)
    tmp = sum(lst2)
    for i in range(n):
        a = a_lst[i]
        print(tmp - (lst1[a] - 1))


def __starting_point():
    main()


__starting_point()
