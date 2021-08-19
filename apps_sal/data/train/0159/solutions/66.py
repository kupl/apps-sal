class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        deque = []
        for (i, num) in enumerate(nums):
            while deque and nums[deque[-1]] < 0:
                deque.pop()
            while deque and deque[0] < i - k:
                deque.pop(0)
            if deque:
                nums[i] = nums[deque[0]] + num
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            deque.append(i)
        return max(nums)
