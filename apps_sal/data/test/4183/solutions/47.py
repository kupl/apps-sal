import math


def lcm(x, y):
    return x * y // math.gcd(x, y)


def main():
    n = int(input())
    t_lst = [int(input()) for _ in range(n)]
    t_lst.sort()
    answer = t_lst[0]
    for i in range(1, n):
        t = t_lst[i]
        answer = lcm(answer, t)

    print(answer)


def __starting_point():
    main()


__starting_point()
