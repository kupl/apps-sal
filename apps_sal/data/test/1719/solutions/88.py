import numpy as np
import re
mod = 10 ** 9 + 7
letters = 'ACGT'


def to_int(s):
    res = 0
    for x in s:
        res <<= 2
        res += letters.index(x)
    return res


def to_str(x, digit):
    res = ''
    for _ in range(digit):
        res += letters[x & 3]
        x >>= 2
    return res[::-1]


def is_ok(s):
    ng = ['AGC', 'ACG', 'GAC', 'A.GC', 'AG.C']
    for x in ng:
        if re.search(x, s):
            return False
    return True


A = [[0] * 64 for _ in range(64)]
for i in range(64):
    s = to_str(i, 3)
    for j in range(4):
        t = s + to_str(j, 1)
        if is_ok(t):
            A[i][to_int(t[1:])] = 1
A = np.array(A, dtype='object')


def mat_power(A, p, mod):
    res = np.eye(A.shape[0], dtype='object')
    while p:
        if p & 1:
            res = np.dot(res, A) % mod
        A = np.dot(A, A) % mod
        p >>= 1
    return res


x = [0] * 64
x[63] = 1
x = np.array(x)
N = int(input())
print((np.dot(mat_power(A, N, mod), x) % mod).sum() % mod)
