class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        dp = [0, 0]
        res = cur = 0
        for i in arr:
            cur ^= i & 1
            res += cur + dp[1 - cur]
            dp[cur] += 1
        return res % (10 ** 9 + 7)
