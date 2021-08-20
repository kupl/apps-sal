class Solution:

    def helper(self, n):
        if n in self.dp:
            return self.dp[n]
        if n < 0:
            return float('inf')
        elif n == 0:
            return 0
        ret = self.helper(n - 1)
        if n % 3 == 0:
            ret = min(ret, self.helper(n - 2 * (n // 3)))
        if n % 2 == 0:
            ret = min(ret, self.helper(n // 2))
        self.dp[n] = 1 + ret
        return self.dp[n]

    def minDays(self, n: int) -> int:
        """
        # DFS => MLE
        sys.setrecursionlimit(2000000000)
        self.dp = {}
        return self.helper(n)
        """
        '\n        # BFS\n        '
        q = [n]
        step = 0
        while q:
            nxts = set()
            for nn in q:
                if nn == 0:
                    return step
                nxts.add(nn - 1)
                if nn % 2 == 0:
                    nxts.add(nn // 2)
                if nn % 3 == 0:
                    nxts.add(nn - 2 * (nn // 3))
            step += 1
            q = deque(nxts)
