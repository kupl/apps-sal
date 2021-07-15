class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        uf = {}
        seen = [0] * (len(arr) + 1)

        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            seen[find(y)] += seen[find(x)]
            uf[find(x)] = find(y)

        ans, n = -1, len(arr)
        for i, a in enumerate(arr, 1):
            seen[a] = 1
            for b in [a - 1, a + 1]:
                if 1 <= b <= n and seen[b]:
                    if seen[find(b)] == m:
                        ans = i - 1
                    union(a, b)
        for i in range(1, n + 1):
            if seen[find(i)] == m:
                ans = n

        return ans
                
                
                
                
                

