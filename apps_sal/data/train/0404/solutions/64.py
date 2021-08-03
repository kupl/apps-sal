class Solution:
    def largestSumOfAverages(self, A: List[int], k: int) -> float:
        n = len(A)
        pre = list(itertools.accumulate([0] + A))
        dp = {}

        def dfs(i, k):
            if (i, k) in dp:
                return dp[(i, k)]
            if k == 1:
                dp[(i, k)] = (pre[-1] - pre[i]) / (n - i)
                return dp[(i, k)]
            ans = -float('inf')
            cur = 0
            for j in range(i, n - k + 1):
                ans = max(ans, (pre[j + 1] - pre[i]) / (j - i + 1) + dfs(j + 1, k - 1))
            dp[(i, k)] = ans
            return ans
        return dfs(0, k)
