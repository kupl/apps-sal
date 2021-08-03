#!/usr/bin/env python3
def pre_calcularion():
    num_max = 10 ** 5
    lst = [True] * (num_max + 1)
    lst[0] = 0
    lst[1] = 0
    for n in range(2, int(num_max ** 0.5) + 1):
        for i in range(2 * n, num_max + 1, n):
            lst[i] = False
    cumsum_lst = [0] * (num_max + 1)
    cal = 0
    for n in range(num_max + 1):
        res = (n + 1) // 2
        if n % 2 == 1 and lst[n] and lst[res]:
            cal += 1
        cumsum_lst[n] = cal
    return cumsum_lst


def main():
    Q = int(input())
    lst = pre_calcularion()
    for _ in range(Q):
        left, right = list(map(int, input().split()))
        print((lst[right] - lst[left - 1]))


def __starting_point():
    main()


__starting_point()
