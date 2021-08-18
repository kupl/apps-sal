from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums, k):
        if max(nums) <= 0:
            return max(nums)
        if min(nums) >= 0:
            return sum(nums)

        N, queue = len(nums), deque()
        dp = [val for val in nums]
        for i, val in enumerate(nums):
            if queue and (i - queue[0] > k):
                queue.popleft()
            if queue and dp[queue[0]] > 0:
                dp[i] += dp[queue[0]]
            while queue and dp[i] >= dp[queue[-1]]:
                queue.pop()
            queue.append(i)
        return max(dp)
