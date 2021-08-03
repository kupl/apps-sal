from math import log, inf
from itertools import product, permutations


def comp_key(p, A, mode):
    a = log(A[p[0][1]]) * A[p[0][2]] if p[1] else log(A[p[0][1]]) + log(A[p[0][2]])
    k = A[p[0][0]] if mode else 1 / A[p[0][0]]
    return a + log(log(k)) if k > 1 else -inf


def solve(A):
    mode = any((x > 1 for x in A))
    c = (max if mode else min)(((x, y) for y in [True, False] for x in permutations(list(range(3)))), key=lambda p: comp_key(p, A, mode))
    k = 'xyz'
    return ('{0}^{1}^{2}' if c[1] else '({0}^{1})^{2}').format(k[c[0][0]], k[c[0][1]], k[c[0][2]])


A = [float(s) for s in input().split()]
print(solve(A))
