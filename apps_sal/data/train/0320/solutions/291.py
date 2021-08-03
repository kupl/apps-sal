class Solution:
    def minOperations(self, nums: List[int]) -> int:
        divied2 = 0
        res = 0
        for i in nums:
            temp = 0
            while i > 0:
                if i % 2 == 0:
                    i //= 2
                    temp += 1
                else:
                    i -= 1
                    res += 1
                divied2 = max(divied2, temp)
            # print(res)
        return res + divied2

        # max_ = max(nums)
        # dp = [(float('inf'),float('inf'),float('inf'))]*(max_+1)
        # dp[0] = (0,0,0)
        # dp[1] = (1,1,0)
        # dp[2] = (2,1,1)
        # for i in range(3, len(dp)):
        #     if i % 2 == 0:
        #         if dp[i//2][0]+1 > dp[i-1][0]+1:
        #             dp[i] = (dp[i-1][0]+1, dp[i-1][1]+1, dp[i-1][2])
        #         else:
        #             dp[i] = (dp[i//2][0]+1, dp[i-1][1], dp[i-1][2]+1)
        #     else:
        #         dp[i] = (dp[i-1][0]+1, dp[i-1][1]+1, dp[i-1][2])
        # print(dp)
        # temp = 0
        # res = 0
        # for i in nums:
        #     temp = max(temp, dp[i][2])
        #     res += dp[i][1]
