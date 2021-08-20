class UnionFind:

    def __init__(self, maxval):
        self.arr = [i for i in range(maxval)]

    def find(self, n):
        if n != self.arr[n]:
            self.arr[n] = self.find(self.arr[n])
        return self.arr[n]

    def union(self, a, b):
        self.arr[self.find(a)] = self.arr[self.find(b)]


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        maxval = max(A) + 1
        oUnionFind = UnionFind(maxval)
        for i in A:
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    oUnionFind.union(i, j)
                    oUnionFind.union(i, i // j)
        counter = collections.defaultdict(int)
        for i in A:
            counter[oUnionFind.find(i)] += 1
        return max(list(counter.values()))
