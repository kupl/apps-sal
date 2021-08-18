import collections
import heapq
import bisect
import math


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solve(A):
    A = [(a, i) for i, a in enumerate(A)]
    A.sort(reverse=True)

    out = 0
    for i in range(len(A)):
        out += (i * A[i][0] + 1)

    print(out)
    print(' '.join(str(i + 1) for _, i in A))


q = 1
tests = []
for test in range(1):
    n = input()
    tests.append([int(p) for p in input().split(' ')])
for test in tests:
    solve(test)
