class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        answer = -1
        n = len(arr)
        parent = {}
        size = {}
        sizes = 0

        def root(x):
            return x if parent[x] == x else root(parent[x])

        def merge(x, y):
            nonlocal sizes
            x = root(x)
            y = root(y)
            if size[y] == m:
                sizes -= 1
            if size[x] < size[y]:
                (x, y) = (y, x)
            parent[y] = x
            size[x] += size[y]
            del size[y]
        for (t, x) in enumerate(arr):
            parent[x] = x
            size[x] = 1
            if x + 1 in parent:
                merge(x, x + 1)
            if x - 1 in parent:
                merge(x, x - 1)
            if size[root(x)] == m:
                sizes += 1
            if sizes:
                answer = t + 1
        return answer
