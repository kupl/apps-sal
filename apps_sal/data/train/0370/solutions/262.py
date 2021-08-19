# Largest Component Size by Common Factor
# https://www.youtube.com/watch?v=6Ud_4A9qTp4

from math import sqrt
from collections import Counter


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        parent = {}

        def ufind(a):
            if a not in parent:
                parent[a] = a
            if a != parent[a]:
                parent[a] = ufind(parent[a])
            return parent[a]

        def uunion(a, b):
            ua = ufind(a)
            ub = ufind(b)

            parent[ua] = ub

        count = Counter()
        for x in A:
            y = 2
            factors = []
            # # 1
            # find common & primes of X
            while x >= y * y:
                if x % y == 0:
                    factors.append(y)
                    # delete y common
                    while x % y == 0:
                        x //= y
                y += 1
            if x > 1:  # find new primes
                factors.append(x)

            # # 2
            # zip(factors, factors[1:]) -> [a,b,c] => ab , bc ~~
            # Linking parent (if link => small -> large)
            for a, b in zip(factors, factors[1:]):
                uunion(a, b)

            # # 3
            # prime > 0
            # minimum factors += 1
            if len(factors) > 0:
                count[factors[0]] += 1

        final_count = Counter()

        for key in count.keys():
            final_count[ufind(key)] += count[key]

        best = 0
        for key in final_count.keys():
            best = max(best, final_count[key])

        return best
