import math
import numpy as np
import sys
input = sys.stdin.readline


def main():
    (s, p) = list(map(int, input().split()))
    i = 1
    while i ** 2 <= p:
        if s == i + p / i:
            print('Yes')
            return 0
        i += 1
    print('No')


main()
