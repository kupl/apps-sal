from copy import copy, deepcopy
import unittest
from io import StringIO
import math
import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input():
    return sys.stdin.readline().strip()


def resolve():
    (N, K) = map(int, input().split())
    A = list(map(int, input().split()))

    def make_divisors(n):
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        divisors.sort(reverse=True)
        return divisors
    M = make_divisors(sum(A))

    def main():
        for i in M:
            AA = [0] * N
            age = 0
            for j in range(N):
                AA[j] = A[j] % i
                age += i - AA[j]
            AA.sort()
            times = 10 ** 9
            sage = 0
            for j in range(0, N - 1):
                sage += AA[j]
                age -= i - AA[j]
                if sage % i == age % i:
                    times = min(max(sage, age), times)
            if times <= K:
                return i
    print(main())


resolve()
