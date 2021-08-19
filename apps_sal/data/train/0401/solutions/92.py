class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0 for i in range(3)]
        for num in nums:
            tmp = dp[:]
            for remainder in range(3):
                dp[(tmp[remainder] + num) % 3] = max(dp[(tmp[remainder] + num) % 3], tmp[remainder] + num)
            # print('num, dp', num, dp)
        return dp[0]
