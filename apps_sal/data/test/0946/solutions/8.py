#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    input()
    arr = list(map(int, input().split()))
    if arr.count(1):
        print('HARD')
    else:
        print('EASY')


def __starting_point():
    main()

__starting_point()
