import os
import sys

import numpy as np
from numpy.linalg import matrix_power

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")

L, A, B, M = list(map(int, sys.stdin.readline().split()))
MOD = M


class ModInt:
    def __init__(self, value):
        self.value = value % MOD

    def __add__(self, other):
        if isinstance(other, ModInt):
            return ModInt(self.value + other.value)
        else:
            return ModInt(self.value + other)

    def __mul__(self, other):
        if isinstance(other, ModInt):
            return ModInt(self.value * other.value)
        else:
            return ModInt(self.value * other)

    def __repr__(self):
        return str(self.value)


size = 0
vec = [ModInt(0), ModInt(A), ModInt(B)]
digits = 1
while size < L:
    cnt = max(0, (10 ** digits - 1 - A) // B - size + 1)
    cnt = min(cnt, L - size)

    mat = np.array([
        [ModInt(pow(10, digits, MOD)), ModInt(0), ModInt(0)],
        [ModInt(1), ModInt(1), ModInt(0)],
        [ModInt(0), ModInt(1), ModInt(1)],
    ])
    if cnt > 0:
        vec = np.dot(vec, matrix_power(mat, cnt))
    digits += 1
    size += cnt
print((vec[0]))
