class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = deque([0])
        ans = nums[0]
        for i in range(1, len(nums)):
            nums[i] += max(nums[q[0]], 0)
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            if i - q[0] == k:
                q.popleft()
            ans = max(ans, nums[i])
        return ans
