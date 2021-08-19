from typing import List
from collections import defaultdict
import time

DEBUG = False
# DEBUG = True


def debug(*args):
    if not DEBUG:
        return
    print((*args))


class Sieve:
    def __init__(self, max_n):
        self.prime_factors = defaultdict(list)
        for i in range(2, max_n + 1):
            if len(self.prime_factors[i]) > 0:
                continue
            for j in range(i, max_n + 1, i):
                self.prime_factors[j].append(i)

    def factors(self, n):
        return self.prime_factors[n]


sieve = Sieve(100000)

# s = Sieve(10000)
# print(s.factors(6))
# print(s.factors(512))
# print(s.factors(1007))
# print(s.factors(5040))


class Solution:
    def largestComponentSize(self, a: List[int]) -> int:
        # start = time.time()
        #
        by_factors = defaultdict(list)
        for x in a:
            for f in sieve.factors(x):
                by_factors[f].append(x)

        seen = set()
        seenf = set()
        ans = 0

        for x in a:
            if x in seen:
                continue
            seen.add(x)
            streak = 1
            todo = [f for f in sieve.factors(x) if f not in seenf]
            while len(todo) > 0:
                f = todo.pop()
                seenf.add(f)
                for cousin in by_factors[f]:
                    if cousin not in seen:
                        seen.add(cousin)
                        streak += 1
                        for ff in sieve.factors(cousin):
                            if ff not in seenf:
                                todo.append(ff)
                                seenf.add(ff)
            ans = max(ans, streak)

        # end = time.time()
        # print(end - start)
        return ans
