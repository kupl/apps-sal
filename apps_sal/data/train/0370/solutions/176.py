class Solution:
    def find(self, i, parent):
        if parent[i] == -1:
            return i
        parent[i] = self.find(parent[i], parent)
        return parent[i]

    def union(self, i, j, parent):
        rooti = self.find(i, parent)
        rootj = self.find(j, parent)
        if rooti != rootj:
            parent[rooti] = rootj

    def largestComponentSize(self, A: List[int]) -> int:
        hm = defaultdict(int)
        parent = [-1] * (100001)
        for i in A:
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    self.union(i, j, parent)
                    self.union(i // j, i, parent)
        for i in A:
            parenti = self.find(i, parent)
            hm[parenti] += 1
        return max(hm.values())
