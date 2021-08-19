class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return m
        parent = [-1] * n
        size = [0] * n

        def find(x):
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return False
            if size[px] > size[py]:
                size[px] += size[py]
                parent[py] = px
            else:
                size[py] += size[px]
                parent[px] = py
            return True
        ans = -1
        for (step, i) in enumerate(arr):
            i -= 1
            size[i] = 1
            for j in (i - 1, i + 1):
                if 0 <= j < n:
                    if size[find(j)] == m:
                        ans = step
                    if size[j]:
                        union(i, j)
        return ans
