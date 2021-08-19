#!/usr/bin/env python3

def main():
    n = int(input())
    arr = [int(a) for a in input().split()]
    arr.sort()
    print(arr[len(arr) // 2 - 1 + len(arr) % 2])


def __starting_point():
    main()


__starting_point()
