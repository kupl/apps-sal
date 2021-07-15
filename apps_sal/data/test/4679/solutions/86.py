#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    A = input()
    B = input()
    C = input()

    w = 'a'
    while True:
        if w == 'a':
            if A == '':
                print('A')
                return
            w = A[0]
            A = A[1:]
        if w == 'b':
            if B == '':
                print('B')
                return
            w = B[0]
            B = B[1:]
        if w == 'c':
            if C == '':
                print('C')
                return
            w = C[0]
            C = C[1:]


def __starting_point():
    main()

__starting_point()
