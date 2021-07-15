class Union_Find():
    def __init__(self):
        self.father = {}
        self.count = collections.defaultdict(int)
    
    def find(self, a):
        if self.father[a] == a:
            return a
        self.father[a] = self.find(self.father[a])
        return self.father[a]
    
    def union(self, a, b):
        father_a = self.find(a)
        father_b = self.find(b)
        if father_a != father_b:
            self.father[father_b] = father_a
            self.count[father_a] += self.count[father_b]


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        uf = Union_Find()
        result = -1
        for i in range(len(arr)):
            uf.father[arr[i]] = arr[i]
            uf.count[arr[i]] = 1
            if arr[i] - 1 in uf.father:
                if uf.count[uf.find(arr[i] - 1)] == m:
                    result = i
                uf.union(arr[i], arr[i] - 1)
            if arr[i] + 1 in uf.father:
                if uf.count[uf.find(arr[i] + 1)] == m:
                    result = i
                uf.union(arr[i], arr[i] + 1)
        n = len(arr)
        for i in range(n):
            if uf.count[uf.find(i + 1)] == m:
                return n
        return result

