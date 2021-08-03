from copy import copy


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


def __starting_point():
    for _ in range(int_inp()):
        str = input()
        if str.endswith('po'):
            print('FILIPINO')
        elif str.endswith('desu') or str.endswith('masu'):
            print('JAPANESE')
        elif str.endswith('mnida'):
            print('KOREAN')


__starting_point()
