# coding: utf-8
from collections import defaultdict


def main():
    N = int(input())
    dic = defaultdict(int)
    max_p = 0

    for i in range(N):
        dic[input()] += 1

    d = dict(dic)
    l = []

    for key, value in list(d.items()):
        l.append([key, value])
        if max_p < value:
            max_p = value

    l.sort(key=lambda x: (-x[1], x[0]), reverse=False)

    for i, j in l:
        if j == max_p:
            print(i)
        else:
            break


def __starting_point():
    main()


__starting_point()
