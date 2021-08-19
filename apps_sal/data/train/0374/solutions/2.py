class Solution:

    def shortestSuperstring(self, A: List[str]) -> str:
        n = len(A)
        overlaps = [[0] * n for x in range(n)]
        for (i, x) in enumerate(A):
            for (j, y) in enumerate(A):
                if i != j:
                    for l in range(min(len(x), len(y)), -1, -1):
                        if x.endswith(y[:l]):
                            overlaps[i][j] = l
                            break
        dp = [[-1] * n for x in range(1 << n)]
        parent = [[None] * n for x in range(1 << n)]
        for mask in range(1, 1 << n):
            for bit in range(n):
                if mask >> bit & 1:
                    pmask = mask ^ 1 << bit
                    if pmask == 0:
                        dp[mask][bit] = 0
                        continue
                    for i in range(n):
                        if pmask >> i & 1:
                            value = dp[pmask][i] + overlaps[i][bit]
                            if value > dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = i
        print(dp)
        perm = []
        mask = (1 << n) - 1
        i = 0
        for (j, val) in enumerate(dp[-1]):
            if val > dp[-1][i]:
                i = j
        while i is not None:
            perm.append(i)
            (mask, i) = (mask ^ 1 << i, parent[mask][i])
        perm = perm[::-1]
        '\n        seen = [False] *n\n        for x in perm:\n            seen[x] = True\n        perm.extend([i for i in range(n) if not seen[i]])\n        '
        ans = [A[perm[0]]]
        for i in range(1, len(perm)):
            overlap = overlaps[perm[i - 1]][perm[i]]
            ans.append(A[perm[i]][overlap:])
        return ''.join(ans)
