class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        deque = collections.deque()
        for i in range(len(nums)):
            if deque:
                nums[i] += deque[0]
            while deque and nums[i] > deque[-1]:
                deque.pop()
            if nums[i] > 0:
                deque.append(nums[i])
            if i >= k and deque and (deque[0] == nums[i - k]):
                deque.popleft()
        return max(nums)
