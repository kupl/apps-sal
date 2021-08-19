class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = len(arr)
        parent = {}
        size = {}
        ds_sizes = Counter()

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def decrement_size(x):
            ds_sizes[x] -= 1
            if ds_sizes[x] == 0:
                del ds_sizes[x]

        def union(x, y):
            (px, py) = (find(x), find(y))
            if px is py:
                return
            if size[px] < size[py]:
                (px, py) = (py, px)
            parent[py] = px
            decrement_size(size[px])
            decrement_size(size[py])
            size[px] += size[py]
            ds_sizes[size[px]] += 1

        def make_set(x):
            if x in parent:
                return
            parent[x] = x
            size[x] = 1
            ds_sizes[1] += 1
        steps = 0
        last_step = -1
        for n in arr:
            make_set(n)
            for neighbor in (n + 1, n - 1):
                if neighbor in parent:
                    union(n, neighbor)
            steps += 1
            if m in ds_sizes:
                last_step = steps
        return last_step
