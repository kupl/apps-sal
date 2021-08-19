import os
import sys


def main():
    N = int(input())
    S = input()
    T = ''
    for s in S:
        T += s
        if len(T) >= 3 and T[-3:] == 'fox':
            T = T[:-3]
    print(len(T))


def __starting_point():
    main()


__starting_point()
