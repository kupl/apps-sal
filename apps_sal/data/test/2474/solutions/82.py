from sys import stdin
import sys
import numpy as np
import collections
from functools import cmp_to_key
import heapq
sys.setrecursionlimit(100000)

##  input functions for me
def rsa(sep = ''):
    if sep == '' :
        return input().split() 
    else: return input().split(sep)
def rip(sep = ''):
    if sep == '' :
        return list(map(int, input().split())) 
    else: return list(map(int, input().split(sep)))
def ria(sep = ''): 
    return list(rip(sep))
def ri(): return int(input())
def rd(): return float(input())
def rs(): return input()
##
class mint:
    mod = int(1e9 + 7)
    def __init__(self, v = 0):
        if not ((v >= 0) and (v < mint.mod)):
            v %= mint.mod
            if v < 0: v += mint.mod
        self.V = v
    def __add__(self, other):
        v = self.V + (other.V if isinstance(other, mint) else other)
        return mint(v)
    def __sub__(self, other):
        v = self.V - (other.V if isinstance(other, mint) else other)
        return mint(v)
    def __mul__(self, other):
        v = self.V * (other.V if isinstance(other, mint) else other)
        return mint(v)
    def __floordiv__(self, other):
        v = self.V * mint.inv((other.V if isinstance(other, mint) else other))
        return mint(v)
    def __truediv__(self, other):
        v = self.V * mint.inv((other.V if isinstance(other, mint) else other))
        return mint(v)
    
    def __eq__(self, other):
        return self.V == (other.V if isinstance(other, mint) else mint(other).V)
    def __ne__(self, other):
        return self.V != (other.V if isinstance(other, mint) else other)
    def __int__(self): return self.V
    # right operand
    def __radd__(self, other):
        v = (other.V if isinstance(other, mint) else other) + self.V
        return mint(v)
    def __rsub__(self, other):
        v = (other.V if isinstance(other, mint) else other) - self.V
        return mint(v)
    def __rmul__(self, other):
        v = (other.V if isinstance(other, mint) else other) * self.V
        return mint(v)
    def __rfloordiv__(self, other):
        v = (other.V if isinstance(other, mint) else other) * mint.inv(self.V)
        return mint(v)
    def __rtruediv__(self, other):
        v = (other.V if isinstance(other, mint) else other) * mint.inv(self.V)
        return mint(v)

    @staticmethod
    def inv(x):
        a, _, _ = mint.extGCD(x, mint.mod)
        return (a + mint.mod) % mint.mod
    @staticmethod
    def extGCD(x, y):
        r0 = x
        r1 = y
        a0 = 1
        a1 = 0
        b0 = 0
        b1 = 1
        while(r1 > 0):
            q1 = r0 // r1
            r2 = r0 % r1
            a2 = a0 - q1 * a1
            b2 = b0 - q1 * b1
            r0 = r1; r1 = r2
            a0 = a1; a1 = a2
            b0 = b1; b1 = b2
        c = r0
        a = a0
        b = b0       
        return a, b, c
    @staticmethod
    def pow(x, k):
        x = x.V if isinstance(x, mint) else x
        return pow(x, k, mint.mod)

    
    def __str__(self):
        return str(self.V)
    def __repr__(self):
        return str(self.V)

def main():
    N = ri()
    A = ria()
    A = sorted(A)
    A = list(reversed(A))
    Pow2 = [mint(0)] * (N + 1)
    Pow2[0] = mint(1)
    for i in range(1,N+1): Pow2[i] = Pow2[i-1] * 2

    tot = mint(0)
    for i in range(N):
        tot += mint(A[i]) * Pow2[N-1]
        if i > 0: tot += mint(A[i]) * i * Pow2[N-2]
    tot *= Pow2[N]
    print(tot)

def __starting_point():
    main()

__starting_point()
