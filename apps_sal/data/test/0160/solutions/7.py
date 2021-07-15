from copy import copy, deepcopy
# from functools import reduce
# from heapq import heapify, heappop, heappush
# from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
import unittest
from io import StringIO
import math
# import numpy as np  # Pythonのみ！
# from operator import xor
# import re
# from scipy.sparse.csgraph import connected_components  # Pythonのみ！
# ↑cf.  https://note.nkmk.me/python-scipy-connected-components/
# from scipy.sparse import csr_matrix
# import string
import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    def make_divisors(n):
        divisors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:  # 平方数の場合n**0.5を1つだけにしてる
                    divisors.append(n//i)

        divisors.sort(reverse=True)  # ソートしたけりゃして
        return divisors

    M = make_divisors(sum(A))

    def main():
        for i in M:
            AA = [0]*N
            age = 0
            # delete = 0
            for j in range(N):
                AA[j] = A[j] % i
                #if AA[j] == 0:
                    # delete += 1
                    # age -= i
                age += i-AA[j]
            AA.sort()

            times = 10**9
            sage = 0
            for j in range(0,N-1):
                sage += AA[j]
                age -= i-AA[j]
                if sage % i == age % i:
                    times = min(max(sage, age), times)
            if times <= K:
                return i
    print(main())

resolve()
