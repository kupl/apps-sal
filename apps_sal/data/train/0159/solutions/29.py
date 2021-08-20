class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        deq = deque()
        for (index, val) in enumerate(nums):
            nums[index] += deq[0] if deq else 0
            while deq and nums[index] > deq[-1]:
                deq.pop()
            if nums[index] > 0:
                deq.append(nums[index])
            if index >= k and deq and (deq[0] == nums[index - k]):
                deq.popleft()
        return max(nums)
