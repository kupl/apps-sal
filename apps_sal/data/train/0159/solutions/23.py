from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums, k):
        if max(nums) <= 0:
            return max(nums)
        if min(nums) >= 0:
            return sum(nums)

        queue, N = deque(), len(nums)
        for i in range(N):
            while queue and queue[0] < i - k:
                queue.popleft()
            if queue:
                nums[i] += nums[queue[0]]
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            if nums[i] > 0:
                queue.append(i)
        return max(nums)
