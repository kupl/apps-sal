class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:

        def find(x):
            while x != par[x]:
                par[x] = par[par[x]]
                x = par[x]
            return x

        def union(x, y):
            nonlocal count
            (px, py) = (find(x), find(y))
            if px == py:
                return
            if size[px] == m:
                count -= 1
            if size[py] == m:
                count -= 1
            if size[px] > size[py]:
                par[py] = par[px]
                size[px] += size[py]
                if size[px] == m:
                    count += 1
            else:
                par[px] = par[py]
                size[py] += size[px]
                if size[py] == m:
                    count += 1
        count = 0
        n = len(arr) + 2
        par = list(range(n))
        size = [0] * n
        res = -1
        for (i, el) in enumerate(arr, 1):
            size[el] = 1
            if m == 1:
                count += 1
            if size[el - 1]:
                union(el, el - 1)
            if size[el + 1]:
                union(el, el + 1)
            if count > 0:
                res = i
        return res
