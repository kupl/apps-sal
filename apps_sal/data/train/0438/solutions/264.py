class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return n
        size = [0] * (n + 1)
        parents = list(range(n + 1))

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            px, py = find(x), find(y)
            if size[px] < size[py]:
                px, py = py, px
            parents[py] = px
            size[px] += size[py]

        result = -1
        for j, i in enumerate(arr):
            size[i] = 1
            if i > 1 and size[find(i - 1)] == m:
                result = j
            if i < n and size[find(i + 1)] == m:
                result = j
            if i > 1 and size[i - 1]:
                union(i, i - 1)
            if i < n and size[i + 1]:
                union(i, i + 1)
        return result
