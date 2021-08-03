class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque, max_deque = deque(), deque()
        l = r = 0
        ans = 0
        while r < len(nums):
            while min_deque and nums[r] <= nums[min_deque[-1]]:
                min_deque.pop()
            while max_deque and nums[r] >= nums[max_deque[-1]]:
                max_deque.pop()
            min_deque.append(r)
            max_deque.append(r)
            if nums[max_deque[0]] - nums[min_deque[0]] <= limit:
                ans = max(ans, r - l + 1)
                r += 1
            elif nums[max_deque[0]] - nums[min_deque[0]] > limit:
                while min_deque[0] <= l:
                    min_deque.popleft()
                while max_deque[0] <= l:
                    max_deque.popleft()
                l += 1

        return ans
