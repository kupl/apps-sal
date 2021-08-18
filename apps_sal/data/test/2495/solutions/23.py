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
import re
import queue


class Scanner():
    @staticmethod
    def int():
        return int(sys.stdin.readline().rstrip())

    @staticmethod
    def string():
        return sys.stdin.readline().rstrip()

    @staticmethod
    def map_int():
        return [int(x) for x in Scanner.string().split()]

    @staticmethod
    def string_list(n):
        return [input() for i in range(n)]

    @staticmethod
    def int_list_list(n):
        return [Scanner.map_int() for i in range(n)]

    @staticmethod
    def int_cols_list(n):
        return [int(input()) for i in range(n)]


class Math():
    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        return Math.gcd(b, a % b)

    @staticmethod
    def lcm(a, b):
        return (a * b) // Math.gcd(a, b)

    @staticmethod
    def roundUp(a, b):
        return -(-a // b)

    @staticmethod
    def toUpperMultiple(a, x):
        return Math.roundUp(a, x) * x

    @staticmethod
    def toLowerMultiple(a, x):
        return (a // x) * x

    @staticmethod
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

    @staticmethod
    def sign(n):
        if n == 0:
            return 0
        if n < 0:
            return -1
        return 1

    @staticmethod
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


class PriorityQueue:
    def __init__(self, l=[]):
        self.__q = l
        heapq.heapify(self.__q)
        return

    def push(self, n):
        heapq.heappush(self.__q, n)
        return

    def pop(self):
        return heapq.heappop(self.__q)


MOD = int(1e09) + 7
INF = int(1e15)


def main():
    N = Scanner.int()
    A = Scanner.map_int()
    s1, s2 = 0, 0
    c1, c2 = 0, 0
    for i in range(N):
        if i % 2 == 0:
            if s1 + A[i] > 0:
                s1 += A[i]
            else:
                c1 += abs(s1 + A[i]) + 1
                s1 = 1
            if s2 + A[i] < 0:
                s2 += A[i]
            else:
                c2 += abs(s2 + A[i]) + 1
                s2 = -1
        else:
            if s1 + A[i] < 0:
                s1 += A[i]
            else:
                c1 += abs(s1 + A[i]) + 1
                s1 = -1
            if s2 + A[i] > 0:
                s2 += A[i]
            else:
                c2 += abs(s2 + A[i]) + 1
                s2 = 1
    print((min(c1, c2)))
    return


def __starting_point():
    main()


__starting_point()
