class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque = collections.deque()
        max_deque = collections.deque()
        left = 0
        right = 0
        max_size = 0
        while right < len(nums):
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()

            min_deque.append(right)
            max_deque.append(right)

            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1

                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            right += 1
            max_size = max(max_size, right - left)
        return max_size
