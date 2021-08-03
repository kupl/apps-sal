class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(x, y):
            xr, yr = find(x), find(y)
            if xr == yr:
                return False
            if sizes[xr] < sizes[yr]:
                (xr, yr) = (yr, xr)

            parent[yr] = xr
            size_counter[sizes[xr]] -= 1
            size_counter[sizes[yr]] -= 1
            sizes[xr] += sizes[yr]
            size_counter[sizes[xr]] += 1

        n = len(arr)
        parent = list(range(n + 1))
        sizes = [1] * (n + 1)
        size_counter = [0] * (n + 1)
        last = -2
        status = [False] * (n + 2)
        for i, x in enumerate(arr):
            status[x] = True
            size_counter[1] += 1
            prev = status[x - 1]
            next = status[x + 1]
            if prev:
                union(x, x - 1)
            if next:
                union(x, x + 1)
            if size_counter[m]:
                last = i

        return last + 1
