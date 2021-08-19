class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        # n = len(nums)
        # hashmap = {0:0}
        # ans = 0
        # sums = 0
        # for i in range(n):
        #     sums += nums[i]
        #     if sums-target in hashmap:
        #         ans = max(ans, hashmap[sums-target] + 1)
        #     hashmap[sums] = ans
        # return ans

        n = len(nums)
        preSum = [0 for i in range(n + 1)]
        hashmap = {0: 0}
        lastend = 0
        ans = 0
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
            begin = hashmap.get(preSum[i] - target, -1)
            if begin >= 0 and begin >= lastend:
                lastend = i
                ans += 1
            hashmap[preSum[i]] = i
        return ans

        # n = len(nums)
        # dp = [0 for i in range(n+1)]
        # for i in range(n):
        #     tmpsum = 0
        #     for j in range(i, -1, -1):
        #         tmpsum += nums[j]
        #         if tmpsum == target:
        #             dp[i+1] = max(dp[i+1], dp[j] + 1)
        #         else:
        #             dp[i+1] = max(dp[i+1], dp[j])
        # print(dp)
        # return dp[n]

        # n = len(nums)
        # dp = [0 for i in range(n)]
        # if target == nums[0]:
        #     dp[0] = 1
        # for i in range(1, n):
        #     tmpsum = 0
        #     for j in range(i, -1, -1):
        #         tmpsum += nums[j]
        #         if tmpsum == target:
        #             if j > 0:
        #                 dp[i] = max(dp[i], dp[j-1] + 1)
        #             else:
        #                 dp[i] = max(dp[i], 1)
        #             break
        # print(dp)
        # return dp[n-1]
