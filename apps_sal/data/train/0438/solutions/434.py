class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        uf = {}
        n, ans = len(arr), -1
        seen = [0] * (n + 1)

        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            seen[find(y)] += seen[find(x)]
            uf[find(x)] = find(y)

        if m == n:
            return n
        for i, a in enumerate(arr):
            seen[a] = 1
            for b in [a - 1, a + 1]:
                if 1 <= b <= n and seen[b]:
                    if seen[find(b)] == m:
                        ans = i
                    union(a, b)
        return ans
