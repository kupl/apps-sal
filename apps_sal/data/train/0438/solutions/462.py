class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        counter = [0] * (n + 1)
        parent = [i for i in range(n + 1)]
        size = [0 for i in range(n + 1)]

        def find(u):
            if parent[u] == u:
                return u
            parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            ru, rv = find(u), find(v)
            if size[ru] < size[rv]:
                parent[ru] = rv
                size[rv] += size[ru]
            else:
                parent[rv] = ru
                size[ru] += size[rv]

        def getSize(p):
            return size[find(p)]

        res = -1
        for i, pos in enumerate(arr):
            size[pos] = 1
            # counter[1] += 1
            if pos > 0:
                if getSize(pos - 1) > 0:
                    s_last = getSize(pos - 1)
                    union(pos - 1, pos)
                    counter[s_last] -= 1
            if pos < n:
                if getSize(pos + 1) > 0:
                    s_next = getSize(pos + 1)
                    union(pos, pos + 1)
                    counter[s_next] -= 1
            counter[getSize(pos)] += 1
            if counter[m] > 0:
                res = i + 1

        return res
