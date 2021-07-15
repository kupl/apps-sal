#!/usr/local/env python3
# -*- encoding: utf-8 -*-
import sys


def readnlines(f_in):
    n = int(f_in.readline().strip())
    s = set()
    content = f_in.readline().strip()
    for i, line in zip(list(range(n)), content.split(' ')):
        if line.isdigit():
            s.add(int(line))
        else:
            s.add(line)
    return s


def print_args():
    print("Recieved {} arguments = {}.".format(len(sys.argv), sys.argv))


def intersect(l1, r1, l2, r2):
    left = max(l1, l2)
    right = min(r1, r2)
    return left, right, max(0, right - left + 1)


def solve():
    m = readnlines(sys.stdin)
    uniques = sorted(m) 
    #print("len(set(m)) = {}".format(len(set(m))))
    #print(uniques)
    if len(uniques) > 3:
        return "NO"
    elif len(uniques) == 3:
        if uniques[2] + uniques[0] == 2 * uniques[1]:
            return "YES"
        return "NO"
    else:
        return "YES"


def __starting_point():
   ans = solve()
   print(ans)

__starting_point()
