class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        parent = [i for i in range(n + 1)]
        size = [0] * (n + 1)
        counter = collections.Counter()

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            (x, y) = (min(x, y), max(x, y))
            (px, py) = (find(x), find(y))
            if px != py:
                counter[size[px]] -= 1
                counter[size[py]] -= 1
                parent[py] = px
                size[px] += size[py]
                counter[size[px]] += 1
        A = [0] * (n + 2)
        res = -1
        for (i, cur) in enumerate(arr):
            A[cur] = 1
            size[cur] = 1
            counter[1] += 1
            if A[cur - 1] == 1:
                union(cur - 1, cur)
            if A[cur + 1] == 1:
                union(cur, cur + 1)
            if counter[m] > 0:
                res = i + 1
        return res
