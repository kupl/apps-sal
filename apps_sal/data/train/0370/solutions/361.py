from math import sqrt, floor
from collections import Counter


class UnionFind:

    def __init__(self, size: int) -> None:
        self.cache = list(range(size + 1))

    def find(self, val: int) -> int:
        if self.cache[val] != val:
            self.cache[val] = self.find(self.cache[val])
        return self.cache[val]

    def union(self, x: int, y: int) -> None:
        self.cache[self.find(x)] = self.cache[self.find(y)]


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        union_find = UnionFind(100000)
        for num in A:
            for factor in range(2, floor(sqrt(num)) + 1):
                if num % factor == 0:
                    union_find.union(num, factor)
                    union_find.union(num, num // factor)

        counter = Counter(map(union_find.find, A))
        return counter.most_common(1)[0][1]
