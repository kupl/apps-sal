class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = [1] * n

    def find(self, x):
        parent = self.parent[x]
        if parent != x:
            self.parent[x] = self.find(parent)
        return self.parent[x]

    def get_count(self, x):
        return self.count[self.find(x)]

    def union(self, x, y):
        xparent, yparent = self.find(x), self.find(y)
        if xparent == yparent:
            return
        self.parent[yparent] = xparent
        self.count[xparent] += self.count[yparent]


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = max(arr)
        bits = [0] * (100005)
        disjoint = UnionFind(n + 1)
        mapping = collections.defaultdict(int)
        ans = -1

        for ind in range(len(arr)):
            pos = arr[ind]
            bits[pos] = 1
            mapping[1] += 1
            i, j = pos - 1, pos + 1
            if bits[i] and disjoint.find(i) != disjoint.find(pos):
                mapping[disjoint.get_count(i)] -= 1
                mapping[disjoint.get_count(pos)] -= 1
                disjoint.union(i, pos)
                mapping[disjoint.get_count(pos)] += 1
            if bits[j] and disjoint.find(j) != disjoint.find(pos):
                mapping[disjoint.get_count(j)] -= 1
                mapping[disjoint.get_count(pos)] -= 1
                disjoint.union(j, pos)
                mapping[disjoint.get_count(pos)] += 1
            if mapping[m] > 0:
                ans = ind + 1
        return ans
