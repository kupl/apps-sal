from copy import copy
from math import *


def arr_float_inp():
    return [float(s) for s in input().split()]


def arr_int_inp():
    return [int(s) for s in input().split()]


def int_inp():
    return int(input())


def float_inp():
    return float(input())


def comp(a):
    return a[0]


def gcd(a, b):
    if b != 0:
        return gcd(b, a % b)
    else:
        return a


def __starting_point():
    n = int_inp()
    arr = arr_int_inp()
    outs = []
    for j in range(len(arr)):
        max_el = (j, arr[j])
        new_arr = [0 for _ in range(len(arr))]
        new_arr[max_el[0]] = max_el[1]
        right = max_el[1]
        for i in range(max_el[0], -1, -1):
            new_arr[i] = min(arr[i], right)
            right = new_arr[i]
        left = max_el[1]
        for i in range(max_el[0], len(arr)):
            new_arr[i] = min(arr[i], left)
            left = new_arr[i]
        outs.append(new_arr)
    max_out = (sum(outs[0]), outs[0])
    for out in outs:
        new_sum = sum(out)
        if new_sum > max_out[0]:
            max_out = (new_sum, out)
    for el in max_out[1]:
        print(el, end=' ')


__starting_point()
