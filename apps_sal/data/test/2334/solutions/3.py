# -*- coding: utf-8 -*-
from math import ceil


def problem(in1, in2, in3):
    n = int(in1)
    balances = list(map(int, in2.split()))

    limit = list(map(int, in3.split()))[0]
    fee = list(map(int, in3.split()))[1]

    tx_size = limit + fee

    tx_count = 0

    for index, balance in enumerate(balances):
        tx_needed = ceil((balance - limit) / tx_size)
        tx_count += tx_needed

    return tx_count * fee


def __starting_point():
    in1 = input()
    in2 = input()
    in3 = input()

    result = problem(in1, in2, in3)

    print(result)


__starting_point()
