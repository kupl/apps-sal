class DisjointSet:
    def __init__(self, size):
        self.parents = list(range(size))
        self.sizes = [1] * size

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x != parent_y:
            self.sizes[parent_x] += self.sizes[parent_y]
            self.parents[parent_y] = parent_x


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        N = len(A)

        def to_divisors(n):
            if n % 6 == 0:
                return [2, 3]
            if n % 3 == 0:
                return [3]
            if n % 2 == 0:
                return [2]
            return []
        maxA = max(A)
        divisors = [to_divisors(i) for i in range(maxA + 1)]
        for i in range(4, maxA + 1):
            if len(divisors[i]) == 0:
                for j in range(i, maxA + 1, i):
                    divisors[j].append(i)
        disjoint_set = DisjointSet(N)
        divisor_to_index = {}
        for i, a in enumerate(A):
            for d in divisors[a]:
                if d in divisor_to_index:
                    disjoint_set.union(i, divisor_to_index[d])
                divisor_to_index[d] = i
        return max(disjoint_set.sizes)
