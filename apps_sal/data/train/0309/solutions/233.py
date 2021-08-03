from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, arr: List[int]) -> int:
        dp = defaultdict(dict)
        n = len(arr)
        max_len = 0
        for i in range(n):
            for j in range(i):
                diff = arr[i] - arr[j]
                dp[i][diff] = dp[j].get(diff, 0) + 1
                max_len = max(max_len, dp[i][diff])

        return max_len + 1
