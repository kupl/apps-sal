#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##################################
# University of Wisconsin-Madison
# Author: Yaqi Zhang
##################################
# This module contains
##################################

# standard library
import sys


def main():
    # nums = list(map(int, input().split()))
    n = int(input())
    s = input()
    assert(len(s) == n)
    digits = list(s)
    m = [0]
    m.extend(list(map(int, input().split())))
    change = False
    for i, ch in enumerate(digits):
        d = int(ch)
        if m[d] > d:
            digits[i] = str(m[d])
            change = True
        else:
            if m[d] < d and change:
                break
    print(''.join(digits))


def __starting_point():
    main()


__starting_point()
