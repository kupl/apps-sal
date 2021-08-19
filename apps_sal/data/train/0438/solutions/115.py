class Solution:

    def findLatestStep(self, arr, m) -> int:
        n = length = len(arr)
        if m == length:
            return m
        parent = [i for i in range(length)]
        size = [0 for _ in range(length)]
        cur = [0] * length
        ans = -1

        def root(p):
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(p, q):
            root_p = root(p)
            root_q = root(q)
            if root_p != root_q:
                if size[root_p] > size[root_q]:
                    parent[root_q] = root_p
                    size[root_p] += size[root_q]
                else:
                    parent[root_p] = root_q
                    size[root_q] += size[root_p]
        for (idx, i) in enumerate(arr):
            i -= 1
            size[i] = 1
            for j in (i - 1, i + 1):
                if 0 <= j < n:
                    if size[root(j)] == m:
                        ans = idx
                    if size[j]:
                        union(i, j)
        return ans
