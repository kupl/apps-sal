from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)

        dp[0] = nums[0]

        ans = dp[0]

        # queue holds the index
        queue = deque([0])

        for j in range(1, len(nums)):
            if queue and queue[0] < j - k:
                queue.popleft()

            dp[j] = nums[j] + max(0, dp[queue[0]])

            while queue and dp[queue[-1]] < dp[j]:
                queue.pop()

            queue.append(j)
            ans = max(ans, dp[j])

        return ans
