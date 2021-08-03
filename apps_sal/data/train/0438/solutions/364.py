class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.size = [0] * (n + 1)
        self.groups = collections.defaultdict(int)
        for i in range(1, n + 1):
            self.parent[i] = i

    def find(self, cur):
        if self.parent[cur] == cur:
            return cur
        self.parent[cur] = self.find(self.parent[cur])
        return self.parent[cur]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.parent[root_b] = root_a
            self.groups[self.size[root_a]] -= 1
            self.groups[self.size[root_b]] -= 1
            self.size[root_a] += self.size[root_b]
            self.groups[self.size[root_a]] += 1


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:

        result = 0
        UF = UnionFind(len(arr))
        for i in range(len(arr)):
            cur = arr[i]
            UF.size[cur] = 1
            UF.groups[1] += 1
            if cur - 1 >= 1 and UF.size[cur - 1] > 0:
                UF.union(cur, cur - 1)
            if cur + 1 <= len(arr) and UF.size[cur + 1] > 0:
                UF.union(cur, cur + 1)
            if m in UF.groups and UF.groups[m] > 0:
                result = i + 1
        return -1 if result == 0 else result
