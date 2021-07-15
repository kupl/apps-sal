class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        dp = [0,0,0]
        for num in nums:
            for i in dp[:]:
                dp[(i+num)%3] = max(dp[(i+num)%3], i+num)
        return dp[0]
    
    # def maxSumDivThree(self, A):
    #     seen = [0, 0, 0]
    #     for a in A:
    #         for i in seen[:]:
    #             seen[(i + a) % 3] = max(seen[(i + a) % 3], i + a)
    #     return seen[0]

