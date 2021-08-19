# -*- coding: utf-8 -*-
import sys
import math
import os
import itertools
import string
import heapq
import _collections
from collections import Counter
from collections import defaultdict
from functools import lru_cache
import bisect


class Scanner():
    def int():
        return int(sys.stdin.readline().rstrip())

    def string():
        return sys.stdin.readline().rstrip()

    def map_int():
        return [int(x) for x in Scanner.string().split()]

    def string_list(n):
        return [input() for i in range(n)]

    def int_list_list(n):
        return [Scanner.map_int() for i in range(n)]

    def int_cols_list(n):
        return [int(input()) for i in range(n)]


class Math():
    def gcd(a, b):
        if b == 0:
            return a
        return Math.gcd(b, a % b)

    def lcm(a, b):
        return (a * b) // Math.gcd(a, b)

    def roundUp(a, b):
        return -(-a // b)

    def toUpperMultiple(a, x):
        return Math.roundUp(a, x) * x

    def toLowerMultiple(a, x):
        return (a // x) * x

    def nearPow2(n):
        if n <= 0:
            return 0
        if n & (n - 1) == 0:
            return n
        ret = 1
        while(n > 0):
            ret <<= 1
            n >>= 1
        return ret

    def isPrime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        d = int(n ** 0.5) + 1
        for i in range(3, d + 1, 2):
            if n % i == 0:
                return False
        return True


MOD = int(1e09) + 7


def main():
    # sys.stdin = open("sample.txt")
    A, B, C = Scanner.map_int()
    ans = 0
    if not A % 2 == B % 2 == C % 2:
        ans += 1
        if A % 2 == B % 2:
            A += 1
            B += 1
        elif B % 2 == C % 2:
            B += 1
            C += 1
        else:
            A += 1
            C += 1
    D = max(A, B, C)
    ans += (D - A) // 2
    ans += (D - B) // 2
    ans += (D - C) // 2
    print(ans)


def __starting_point():
    main()


__starting_point()
