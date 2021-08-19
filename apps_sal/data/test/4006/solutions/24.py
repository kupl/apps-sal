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
    num = int(input())
    seen = set()
    while num:
        if num in seen:
            break
        seen.add(num)
        num += 1
        while num % 10 == 0:
            num //= 10
    print(len(seen))


def __starting_point():
    main()


__starting_point()
