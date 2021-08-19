class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        self.parent = [i for i in range(n + 1)]
        self.rank = [1 for _ in range(n + 1)]
        self.result = 0
        self.groups = set()

        def find_parent(a):
            if a != self.parent[a]:
                self.parent[a] = find_parent(self.parent[a])
            return self.parent[a]

        def union(a, b, check=False):
            parent_a = find_parent(a)
            parent_b = find_parent(b)
            if parent_a == parent_b:
                if self.rank[parent_a] == m:
                    self.groups.add(parent_a)
                return
            if self.rank[parent_a] < self.rank[parent_b]:
                (parent_a, parent_b) = (parent_b, parent_a)
            self.parent[parent_b] = parent_a
            self.rank[parent_a] += self.rank[parent_b]
            if parent_a in self.groups:
                self.groups.remove(parent_a)
            if parent_b in self.groups:
                self.groups.remove(parent_b)
            if check:
                if self.rank[parent_a] == m:
                    self.groups.add(parent_a)
        self.binary = [0 for _ in range(n + 2)]
        result = -1
        for idx in range(n):
            num = arr[idx]
            if self.binary[num - 1] == 1 and self.binary[num + 1] == 1:
                union(num - 1, num)
                union(num, num + 1, True)
            elif self.binary[num - 1] == 1:
                union(num, num - 1, True)
            elif self.binary[num + 1] == 1:
                union(num, num + 1, True)
            else:
                union(num, num, True)
            if len(self.groups) > 0:
                result = idx + 1
            self.binary[num] = 1
        return result
