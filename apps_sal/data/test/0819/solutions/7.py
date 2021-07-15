#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    if k == 1:
        print(min(arr))
    elif k == 2:
        print(max(arr[0], arr[-1]))
    else:
        print(max(arr))
def __starting_point():
    main()

__starting_point()
