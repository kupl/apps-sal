import math
import collections
import itertools
import copy
from collections import deque
import bisect


def gcd(a, b):
    """Euclidean Algorithm"""
    while b != 0:
        (a, b) = (b, a % b)
    return a


def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    while True:
        Min = min(A)
        Max = max(A)
        for i in range(N):
            A[i] = gcd(A[i], Min)
        if Min == Max:
            break
    print(Min)


resolve()
