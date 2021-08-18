class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:

        n, inf = len(arr), float('inf')
        a, s = [[] for _ in range(n)], [(inf, -1)]

        for i, x in enumerate(arr):
            while s[-1][0] < x:
                if s[-1][1] >= i - d:
                    a[i].append(s[-1][1])
                s.pop()
            s.append((x, i))

        s = [(inf, -1)]
        for i, x in reversed(list(enumerate(arr))):
            while s[-1][0] < x:
                if s[-1][1] <= i + d:
                    a[i].append(s[-1][1])
                s.pop()
            s.append((x, i))

        dp, v = [1] * n, [0] * n

        def dfs(i):
            if v[i]:
                return
            v[i] = 1
            for j in a[i]:
                dfs(j)
                dp[i] = max(dp[i], dp[j] + 1)

        for i in range(n):
            dfs(i)
        return max(dp)
