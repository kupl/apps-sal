#!/usr/bin/env python3

def main():
    n = int(input())
    print((len(set([int(input()) for i in range(n)]))))


def __starting_point():
    main()

__starting_point()
