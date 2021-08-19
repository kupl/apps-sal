class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:

        def find(parent, x):
            if x == parent[x]:
                return x
            parent[x] = find(parent, parent[x])
            return parent[x]
        n = len(arr)
        parent = [0 for x in range(n + 1)]
        size = [0] * (n + 1)
        count = [0] * (n + 1)
        ans = -1
        for (i, pos) in enumerate(arr):
            size[pos] = 1
            count[1] += 1
            parent[pos] = pos
            for j in [-1, 1]:
                if pos + j <= n and pos + j > 0 and (parent[pos + j] != 0):
                    x = find(parent, pos + j)
                    y = find(parent, pos)
                    if x != y:
                        count[size[x]] -= 1
                        count[size[y]] -= 1
                        parent[x] = y
                        size[y] += size[x]
                        count[size[y]] += 1
            if count[m] > 0:
                ans = i + 1
        return ans
