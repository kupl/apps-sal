import math


class Solution:

    def __init__(self):
        self.prime_divisors_cache = {}

    def prime_divisors(self, x, i=2):
        if x in self.prime_divisors_cache:
            return self.prime_divisors_cache[x]
        while i * i <= x:
            if x % i != 0:
                i += 1
                if i > 3:
                    i += 1
            else:
                self.prime_divisors_cache[x] = set([i]) | self.prime_divisors(x // i, i)
                return self.prime_divisors_cache[x]

        res = set()
        if x > 1:
            res.add(x)

        self.prime_divisors_cache[x] = res
        return self.prime_divisors_cache[x]

    def largestComponentSize(self, A: List[int]) -> int:
        # related if NOT coprime

        # we can keep associated a list of prime factors with each set

        # integers in A are unique
        # form a disjoint set structure
        # node label -> parent
        parent = dict()
        # representative label -> size of set
        size = dict()
        # keep track of list of representatives for ease
        reps = set()

        def getRep(x):
            # compress path to parent
            while parent[x] != x:
                x, parent[x] = parent[x], parent[parent[x]]
            return x

        # def getSize(x):
        #     return size[getRep(x)]

        def add(x):
            parent[x] = x
            size[x] = 1
            reps.add(x)

        def merge(x, y):
            x = getRep(x)
            y = getRep(y)
            if x == y:
                return
            if size[x] < size[y]:
                x, y = y, x
            size[x] += size.pop(y)
            parent[y] = x
            reps.remove(y)

        # prime -> list of numbers it divides
        prime2dividend = {}
        for x in A:
            add(x)
            for p in self.prime_divisors(x):
                if not p in prime2dividend:
                    prime2dividend[p] = [x]
                else:
                    prime2dividend[p].append(x)

        for _, xs in list(prime2dividend.items()):
            # guaranteed to be one
            first = xs.pop()
            for x in xs:
                merge(first, x)

        return max([size[rep] for rep in reps])
