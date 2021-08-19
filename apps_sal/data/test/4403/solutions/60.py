#!/usr/bin/env python3
import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    S = input()
    print(S.count('+') - S.count('-'))


def __starting_point():
    main()


__starting_point()
