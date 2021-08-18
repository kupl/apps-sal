class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dp = defaultdict(int)
        dp[1] = 0

        def go(i):
            if i == 1:
                return 0
            if dp[i] > 0:
                return dp[i]
            if (i % 2) == 0:
                ans = go(i // 2) + 1
            else:
                ans = go((3 * i) + 1) + 1
            dp[i] = ans
            return ans

        for i in range(lo, hi + 1):
            dp[i] = go(i)
        lis = []
        for i in range(lo, hi + 1):
            lis.append((dp[i], i))
        lis.sort()
        ans = lis[k - 1]
        return ans[1]
