class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        minDeque = collections.deque()
        maxDeque = collections.deque()
        maxlength = 0
        left = 0
        right = 0
        while right < len(nums):
            while maxDeque and nums[right] > nums[maxDeque[-1]]:
                maxDeque.pop()
            maxDeque.append(right)
            while minDeque and nums[right] < nums[minDeque[-1]]:
                minDeque.pop()
            minDeque.append(right)
            while abs(nums[maxDeque[0]] - nums[minDeque[0]]) > limit:
                if maxDeque[0] == left:
                    maxDeque.popleft()
                if minDeque[0] == left:
                    minDeque.popleft()
                left += 1
            maxlength = max(maxlength, right - left + 1)
            right += 1
        return maxlength
