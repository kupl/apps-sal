class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        (q_max, ans) = (deque([(nums[0], 0)]), nums[0])
        for i in range(1, len(nums)):
            nums[i] += max(q_max[0][0], 0)
            if q_max[0][1] <= i - k:
                q_max.popleft()
            while q_max and nums[i] > q_max[-1][0]:
                q_max.pop()
            q_max.append((nums[i], i))
            ans = max(ans, nums[i])
        return ans
