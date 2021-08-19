from typing import List
from collections import defaultdict, deque
from math import sqrt


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        factors = defaultdict(set)
        disjoint = list(range(len(A)))

        def populateFactors():
            for i in range(len(A)):
                a = A[i]
                if a == 1:
                    continue
                x = a
                while x % 2 == 0:
                    factors[2].add(i)
                    x //= 2
                for n in range(3, int(sqrt(x) + 1), 2):
                    while x % n == 0:  # n is a factor
                        factors[n].add(i)
                        x //= n
                        if x <= 1:
                            break
                if x > 1:
                    factors[x].add(i)

        def find(i):
            while disjoint[i] != i:
                i = disjoint[i]
            return i

        def union(i, j):
            disjoint[find(j)] = find(i)

        populateFactors()
        for factor in factors:
            x = None
            for i in factors[factor]:
                if x is None:
                    x = i
                union(x, i)
        count = defaultdict(int)
        for i in range(len(A)):
            count[find(i)] += 1
        return max(count.values())
