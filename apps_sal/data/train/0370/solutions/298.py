class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, A):
        root = A
        while root != self.parent[root]:
            root = self.parent[root]

        while A != root:
            old_parent = self.parent[A]
            self.parent[A] = root
            A = old_parent
        return(root)

    def union(self, A, B):
        root_A = self.find(A)
        root_B = self.find(B)
        if root_A == root_B:
            return(False)

        if self.size[root_A] < self.size[root_B]:
            self.parent[root_A] = root_B
            self.size[root_B] += self.size[root_A]
        else:
            self.parent[root_B] = root_A
            self.size[root_A] += self.size[root_B]

        return(True)


class Solution:
    def gcd(self, a, b):
        if (b == 0):
            return a
        return gcd(b, a % b)

    def largestComponentSize(self, A: List[int]) -> int:
        dsu = UnionFind(max(A) + 1)

        for a in A:
            for factor in range(2, int(sqrt(a)) + 1):
                if a % factor == 0:
                    dsu.union(a, factor)
                    dsu.union(a, a // factor)

        group_count = defaultdict(int)
        for a in A:
            group_id = dsu.find(a)
            group_count[group_id] += 1

        return max(group_count.values())
