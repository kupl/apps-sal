class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # dp = [[0 for i in range(2)]  for j in  range(len(nums) + 1)]
        # res = 0
        # for i, num in enumerate(nums):
        #     if num == 0:
        #         dp[i + 1][0] = dp[i + 1][1] = 0
        #     elif num > 0:
        #         dp[i + 1][0] = dp[i][0] + 1
        #         dp[i + 1][1] = dp[i][1] + 1 if dp[i][1] else 0
        #     else:
        #         dp[i + 1][0] = dp[i][1] + 1 if dp[i][1] else 0
        #         dp[i + 1][1] = dp[i][0] + 1
        #     res = max(res, dp[i + 1][0])
        # return res
        pos_num = neg_num = res = 0
        for i, num in enumerate(nums):
            if num == 0:
                pos_num = neg_num = 0
            elif num > 0:
                neg_num = neg_num + 1 if neg_num else 0
                pos_num += 1
            else:
                cur_pos = pos_num
                pos_num = neg_num + 1 if neg_num else 0
                neg_num = cur_pos + 1
            res = max(res, pos_num)
        return res
