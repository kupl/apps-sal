class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        # result = 1
        # for i in range(len(nums)-2, -1, -1):
        #     for j in range(i+1, len(nums)):
        #         dp[i][j] = max(dp[i][j-1], dp[i+1][j] ,abs(nums[i] - nums[j]))
        #         # print(dp[i][j])
        #         if dp[i][j] <= limit:
        #             result = max(result, j - i + 1)
        # return result
    
        maxq, minq = [], []
        res = i = 0
        for j, a in enumerate(nums):
            heapq.heappush(maxq, [-a, j])
            heapq.heappush(minq, [a, j])
            # print(maxq, minq)
            while -maxq[0][0] - minq[0][0] > limit:
                i = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < i: heapq.heappop(maxq)
                while minq[0][1] < i: heapq.heappop(minq)
            res = max(res, j - i + 1)
            # print(maxq)
            # print(minq)
        return res
