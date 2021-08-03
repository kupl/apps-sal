from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:

        que = deque()
        for ind in range(len(nums)):
            nums[ind] += que[0] if que else 0

            while que and nums[ind] > que[-1]:
                que.pop()

            if nums[ind] > 0:
                que.append(nums[ind])

            if que and ind >= k and que[0] == nums[ind - k]:
                que.popleft()

        return max(nums)
