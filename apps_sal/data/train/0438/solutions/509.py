class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        a = [x - 1 for x in arr]
        n = len(a)
        parent = list(range(n))
        size = [0] * n
        count = Counter()

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            (x, y) = (find(u), find(v))
            if x != y:
                parent[y] = x
                size[x] += size[y]
        res = -1
        bits = [0] * n
        for (i, u) in enumerate(a, 1):
            bits[u] = 1
            size[u] = 1
            count[1] += 1
            if u > 0 and bits[u - 1]:
                count[size[find(u - 1)]] -= 1
                union(u - 1, u)
            if u + 1 < n and bits[u + 1]:
                count[size[find(u + 1)]] -= 1
                union(u, u + 1)
            if size[find(u)] != 1:
                count[1] -= 1
                count[size[find(u)]] += 1
            if count[m] > 0:
                res = i
        return res
