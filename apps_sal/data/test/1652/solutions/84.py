# -*- coding: utf-8 -*-
import sys
import math
import os
import itertools
import _collections
import string
from functools import lru_cache
import heapq

class cin():
    def int():
        return int(sys.stdin.readline().rstrip())
    def string():
        return sys.stdin.readline().rstrip()
    def mapInt():
        return [int(x) for x in cin.string().split()]
    def stringList(n):
        return [input() for i in range(n)]
    def intListList(n):
        return [cin.mapInt() for i in range(n)]
    def intColsList(n):
        return [int(input()) for i in range(n)]
        
class Math():
    def gcd(a,b):
        if b == 0:
            return a
        return Math.gcd(b,a % b)
    def lcm(a,b):
        return (a * b) // Math.gcd(a,b)
    def roundUp(a,b):
        return -(-a // b)
    def toUpperMultiple(a,x):
        return Math.roundUp(a,x) * x
    def toLowerMultiple(a,x):
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
        for i in range(3,d + 1,2):
            if n % i == 0:
                return False
        return True


MOD = int(1e09) + 7

def main():
    S = cin.string()
    while len(S) != 0:
        if S[-5:] == "dream":
            S = S[:-5]
        elif S[-7:] == "dreamer":
            S = S[:-7]
        elif S[-5:] == "erase":
            S = S[:-5]
        elif S[-6:] == "eraser":
            S = S[:-6]
        else:
            print("NO")
            return
    print("YES")
    return

def __starting_point():
    main()

__starting_point()
