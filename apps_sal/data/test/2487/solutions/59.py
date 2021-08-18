import sys
import math
import operator
import itertools
import collections
import heapq
import bisect


class Solution:
    def __init__(self):
        pass

    def solve(self, *Input):
        n, edges = Input
        ans = (n * (n + 2) * (n + 1) // 3) >> 1
        for edge in edges:
            a, b = sorted(edge)
            ans -= a * (n + 1 - b)
        return ans

    def create(self, *Input):
        return []

    def check(self, *Input):
        return True

    def sieve_classic(self, a, b):
        self.primes = [True] * (b + 1)
        self.primes[0] = self.primes[1] = False
        for i in range(2, b + 1):
            if self.primes[i] and i * i <= b:
                for j in range(i * i, b + 1, i):
                    self.primes[j] = False
        self.primes = [x for x, y in enumerate(self.primes) if y]
        ind = bisect.bisect_left(self.primes, a)
        self.primes[:ind] = []
        return None


def __starting_point():
    solution = Solution()

    inputs = iter(sys.stdin.readlines())
    n = int(next(inputs))
    edges = [list(map(int, next(inputs).split())) for _ in range(n - 1)]
    ans = solution.solve(n, edges)
    print(ans)


__starting_point()
