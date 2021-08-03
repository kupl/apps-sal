from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = []
        dp.append(nums[0])
        deq = deque()
        deq.append(0)
        for i in range(1, len(nums)):
            while len(deq) and (i - deq[0]) > k:
                deq.popleft()
            cur_max = dp[deq[0]] if len(deq) and dp[deq[0]] > 0 else 0
            dp.append(cur_max + nums[i])
            while len(deq) and dp[deq[-1]] < dp[i]:
                deq.pop()
            deq.append(i)
        return max(dp)
