import sys
import math


def calculate(A, k, x):
    res = 0
    if abs(k) >= 2:
        for a in reversed(A):
            res = k * res + a
            if abs(res) > x:
                return float('inf')
        return res
    else:
        for a in reversed(A):
            res = k * res + a
        return res


def solve():
    n, k = [int(x) for x in input().split()]
    A = ['?' if line == '?\n' else int(line) for line in sys.stdin]

    if k == 0:
        return A[0] == 0 or A[0] == '?' and (n + 1 - A.count('?')) % 2 == 1
    else:
        if '?' in A:
            return n % 2 == 1
        else:
            return calculate(A, k, 10000) == 0


print('Yes' if solve() else 'No')
