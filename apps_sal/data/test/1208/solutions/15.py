"""
Codeforces
567 B.

@author yamaton
@date 2015-08-05
"""
import sys
import collections


def solve(xs):
    d = collections.defaultdict(int)
    already_in = collections.defaultdict(bool)
    for (sign, person) in xs:
        if sign == '+':
            d[person] += 1
        else:
            d[person] -= 1
        if d[person] < 0:
            already_in[person] = True
    number = sum(dict(already_in).values())
    history = [number]
    for (sign, person) in xs:
        if sign == '+':
            number += 1
        else:
            number -= 1
        history.append(number)
    return max(history)


def main():
    n = int(input())
    xs = [input().strip().split() for _ in range(n)]
    result = solve(xs)
    print(result)


def __starting_point():
    main()


__starting_point()
