class Solution:

    def numOfSubarrays(self, coll: List[int]) -> int:
        n = len(coll)
        m = 10 ** 9 + 7
        dp = [(0, 0) for _ in range(n + 1)]
        for (i, x) in enumerate(coll):
            if x & 1:
                dp[i + 1] = (dp[i][1], dp[i][0] + 1)
            else:
                dp[i + 1] = (dp[i][0] + 1, dp[i][1])
        return sum((odds for (evens, odds) in dp)) % m
