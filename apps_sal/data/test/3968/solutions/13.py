# -*- coding: utf-8 -*-
"""
Created on Fri May  3 23:45:36 2019

@author: plosi
"""
di = {}


def isPrime(n):
    if n == 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    else:
        r = int(n**(1 / 2))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f = f + 6
    return True


def mk_arr(num_ones, num_twos):

    n = 0
    st = ""
    while num_ones > 0 and num_twos > 0:
        if isPrime(n + 1):
            st = st + "1 "
            num_ones = num_ones - 1
            n = n + 1
        else:
            st = st + "2 "
            num_twos = num_twos - 1
            n = n + 2
    if num_twos == 0:
        for i in range(num_ones):
            st = st + "1 "
    if num_ones == 0:
        for i in range(num_twos):
            st = st + "2 "

    return st


def main():
    n = int(input())
    arr = input().split(" ")
    num_ones = 0
    for val in arr:
        if val == "1":
            num_ones = num_ones + 1
    st = mk_arr(num_ones, n - num_ones)
    print(st)


main()
