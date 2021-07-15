#!/usr/bin/env python3
# import sys
# sys.recursionlimit(10**7)
from functools import reduce


def solve(a,b):
    if a <= 8 and b <= 8:
        return "Yay!"
    else:
        return ":("

def main():
    a,b = list(map(int,input().split()))
    print(('{}'.format(solve(a,b))))




def __starting_point():
  main()

__starting_point()
