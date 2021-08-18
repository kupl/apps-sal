class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return len(arr)

        u = list(range(len(arr) + 1))
        size = [0] * (len(arr) + 1)

        def find(a):
            if u[a] != a:
                u[a] = find(u[a])
            return u[a]

        def union(a, b):
            u1 = find(a)
            u2 = find(b)
            if u1 != u2:
                if size[u1] < size[u2]:
                    u[u1] = u2
                    size[u2] += size[u1]
                else:
                    u[u2] = u1
                    size[u1] += size[u2]
        ans = -1
        for a_idx, a in enumerate(arr):
            size[a] = 1
            for i in [a - 1, a + 1]:
                if 1 <= i <= len(arr):
                    if size[find(i)] == m:
                        ans = a_idx
                    if size[i] > 0:
                        union(a, i)

        for i in range(1, len(arr) + 1):
            if size[find(i)] == m:
                return len(arr)
        return ans
