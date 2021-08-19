class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = max(arr)
        dp = [[0, [i, i]] for i in range(n + 2)]
        memo = {}
        res = -1
        for (j, i) in enumerate(arr):
            dp[i][0] = 1
            val = 1
            if dp[i - 1][0]:
                memo[dp[i - 1][0]] -= 1
                (left, right, val) = (dp[i - 1][1][0], i, val + dp[i - 1][0])
                dp[left] = dp[right] = [val, [left, right]]
            if dp[i + 1][0]:
                memo[dp[i + 1][0]] -= 1
                (left, right, val) = (dp[i][1][0], dp[i + 1][1][1], val + dp[i + 1][0])
                dp[left] = dp[right] = [val, [left, right]]
            memo[val] = memo.get(val, 0) + 1
            if memo.get(m, 0):
                res = j + 1
        return res
