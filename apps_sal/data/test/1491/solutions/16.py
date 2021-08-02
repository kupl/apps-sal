# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 19:33:27 2017

@author: ms
"""
from math import sqrt


def main():
    n = int(input())
    piles = [int(x) for x in input().split()]
    spiles = sorted(piles)
    nearest = []
    cost = []
    for a in piles:
        tmp = (int(sqrt(a)))
        lower = tmp**2
        upper = (tmp + 1)**2
        if (a - lower) <= (upper - a):
            nearest.append(lower)
        else:
            nearest.append(upper)
        cost.append(abs(a - nearest[-1]))

    cost = sorted(cost)
    summ = 0
    for i in range(int(n / 2)):
        summ += cost[i]

    for j in range(int(n / 2), n):
        if (cost[j] == 0):
            summ += 1
            if (spiles[j] == 0):
                summ += 1
        else:
            break
    print(summ)


main()
