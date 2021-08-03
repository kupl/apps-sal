class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        n = max(A) + 1
        parent = [i for i in range(n)]
        rank = [0] * n

        for a in A:
            for k in range(2, int(sqrt(a)) + 1):
                if a % k == 0:
                    self.union(parent, a, k, rank)
                    self.union(parent, a, a // k, rank)

        counter = collections.Counter()
        for a in A:
            counter[self.find_root(parent, a)] += 1

        return max(counter.values())

    def find_root(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find_root(parent, parent[x])
        return parent[x]

    def union(self, parent, x, y, rank):
        x_root = self.find_root(parent, x)
        y_root = self.find_root(parent, y)
        if x_root != y_root:
            if rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            elif rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            else:
                parent[x_root] = y_root
                rank[y_root] += 1

    def find_common_factor(self, a, b):
        for i in range(2, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                return True
        return False
