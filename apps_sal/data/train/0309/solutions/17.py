class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 2:
            return n
        
        dp = [{} for i in range(n)]
        res = 0
        for i in range(1, n):
            for j in range(i):
                dis = nums[i] - nums[j]
                # 在前面的dp[j]中 用get()寻找dp中已有的数据。
                # 如果没有，说明是基本状态，用1初始化，+1为2
                x = dp[j].get(dis, 1)+1
                dp[i][dis] = x
            res = max(res, max(dp[i].values()))

        return res


