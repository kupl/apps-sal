class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        degree = [0] * n
        par = list(range(n))

        def find(x: int) -> int:
            if par[x] == x:
                return x
            return find(par[x])

        def union(x: int, y: int) -> None:
            (px, py) = (find(x), find(y))
            if px == py:
                return
            if degree[px] > degree[py]:
                par[py] = px
                degree[px] += degree[py]
            else:
                par[px] = py
                degree[py] += degree[px]
        res = -1
        for (i, num) in enumerate(arr):
            num -= 1
            degree[num] = 1
            for nei in (num - 1, num + 1):
                if 0 <= nei < n:
                    if degree[find(nei)] == m:
                        res = i
                    if degree[nei]:
                        union(nei, num)
        for i in range(n):
            if degree[find(i)] == m:
                return n
        return res
