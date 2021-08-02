import math


def main():
    n, x = map(int, input().split())
    x_lst = list(map(int, input().split()))
    x_lst.sort()

    if n == 1:
        minimum = abs(x_lst[0] - x)
    elif n == 2:
        minimum = abs(x_lst[1] - x_lst[0])
        lst = [abs(x_lst[1] - x), abs(x_lst[0] - x)]
        lst.sort()
        lst.reverse()
        for i in range(2):
            if minimum % lst[i] == 0:
                minimum = lst[i]
                break
    else:
        lst1 = []
        for i in range(n):
            if i != n - 1:
                lst1.append(abs(x_lst[i + 1] - x_lst[i]))

        minimum = math.gcd(lst1[0], lst1[1])
        for i in range(n - 1):
            if i != n - 2:
                minimum = min(minimum, math.gcd(lst1[i], lst1[i + 1]))

        lst2 = []
        for i in range(n):
            lst2.append(abs(x_lst[i] - x))

        lst2.sort()
        lst2.reverse()
        for i in range(n):
            if minimum % lst2[i] == 0:
                minimum = lst2[i]
                break

    print(minimum)


def __starting_point():
    main()


__starting_point()
