import math


class UnionFind:

    def __init__(self, n):
        self.data = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.data[x] != x:
            self.data[x] = self.find(self.data[x])
        return self.data[x]

    def union(self, x, y):
        (ix, iy) = (self.find(x), self.find(y))
        if ix != iy:
            self.data[ix] = iy
            self.size[iy] += self.size[ix]
            self.size[ix] = 0


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        def prime_set(num):
            res = set()
            while num % 2 == 0:
                res.add(2)
                num //= 2
            for i in range(3, int(math.sqrt(num)) + 1, 2):
                while num % i == 0:
                    res.add(i)
                    num //= i
            if num > 2:
                res.add(num)
            return res
        n = len(A)
        uf = UnionFind(n)
        primes_dict = collections.defaultdict(list)
        for (i, num) in enumerate(A):
            pr_set = prime_set(num)
            for p in pr_set:
                primes_dict[p].append(i)
        for indices in primes_dict.values():
            for j in range(1, len(indices)):
                uf.union(indices[j - 1], indices[j])
        return max(collections.Counter((uf.find(i) for i in range(n))).values())

    def gcd_with_bfs(self, A: List[int]) -> int:
        graph = collections.defaultdict(set)
        for i in range(len(A)):
            for j in range(i, len(A)):
                if math.gcd(A[i], A[j]) > 1:
                    graph[A[i]].add(A[j])
                    graph[A[j]].add(A[i])
        res = 0
        seen = set()
        for a in A:
            if a not in seen:
                node_count = 0
                q = collections.deque([a])
                seen.add(a)
                while q:
                    node = q.popleft()
                    node_count += 1
                    seen.add(node)
                    for child in graph[node]:
                        if child not in seen:
                            seen.add(child)
                            q.append(child)
                res = max(res, node_count)
        return res
