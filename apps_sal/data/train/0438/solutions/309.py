class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        L = len(arr)
        parent = [0] * (L + 1)
        size = [1] * (L + 1)

        def find(x):
            if parent[x] == 0:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            if find(x) == find(y):
                return
            px = find(x)
            py = find(y)
            if size[px] < size[py]:
                px, py = py, px

            if size[px] == m:
                good.discard(px)
            if size[py] == m:
                good.discard(py)

            parent[py] = px
            size[px] += size[py]

        bs = [0] * (L + 1)
        ret = -1
        step = 0
        good = set()

        for a in arr:
            step += 1
            bs[a] = 1
            if a - 1 >= 0 and bs[a - 1] == 1:
                union(a, a - 1)
            if a + 1 <= L and bs[a + 1] == 1:
                union(a, a + 1)

            if size[find(a)] == m:
                good.add(find(a))
            if len(good) > 0:
                ret = step

        return ret
