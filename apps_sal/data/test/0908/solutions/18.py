#!/usr/bin/env python3.5
import sys


def read_data():
    n = int(next(sys.stdin))
    prices = list(map(int, next(sys.stdin).split()))
    vocabulary = []
    for i in range(n):
        vocabulary.append(next(sys.stdin).strip())
    return n, prices, vocabulary


def apply_op(sNext, sPrev, curCost, optCost):
    if sNext >= sPrev:
        if optCost is None or curCost < optCost:
            return curCost
    return optCost


def solve(n, prices, vocabulary):
    opt_0, opt_1 = 0, prices[0]
    prevStr = vocabulary[0]
    prevStrReversed = "".join(reversed(prevStr))
    for curStr, curPrice in zip(vocabulary[1:], prices[1:]):
        curStrReversed = "".join(reversed(curStr))
        n_opt0, n_opt1 = None, None
        if opt_0 is not None:
            n_opt0 = apply_op(curStr, prevStr, opt_0, n_opt0)
            n_opt1 = apply_op(curStrReversed, prevStr, opt_0 + curPrice, n_opt1)
        if opt_1 is not None:
            n_opt0 = apply_op(curStr, prevStrReversed, opt_1, n_opt0)
            n_opt1 = apply_op(curStrReversed, prevStrReversed, opt_1 + curPrice, n_opt1)
        opt_0, opt_1 = n_opt0, n_opt1
        prevStr, prevStrReversed = curStr, curStrReversed
        if opt_0 is None and opt_1 is None:
            break
    if opt_0 is None:
        return opt_1
    if opt_1 is None:
        return opt_0
    return min(opt_0, opt_1)


def __starting_point():
    n, prices, vocabulary = read_data()
    sorting_cost = solve(n, prices, vocabulary)
    if sorting_cost != None:
        print(sorting_cost)
    else:
        print(-1)


__starting_point()
