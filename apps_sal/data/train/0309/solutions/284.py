class Solution:
    def longestArithSeqLength(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 2:
            return n
        dp = defaultdict(dict)
        max_len = 2
        for i in range(n):
            for j in range(i + 1, n):
                diff = arr[j] - arr[i]
                if diff in dp[i]:
                    dp[j][diff] = dp[i][diff] + 1
                else:
                    dp[j][diff] = 2
                max_len = max(max_len, dp[j][diff])
        return max_len
