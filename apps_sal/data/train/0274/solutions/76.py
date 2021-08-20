class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_queue = collections.deque()
        min_queue = collections.deque()
        l = r = 0
        max_len = 0
        while r < len(nums):
            while max_queue and nums[r] >= max_queue[-1][0]:
                max_queue.pop()
            max_queue.append((nums[r], r))
            while min_queue and nums[r] <= min_queue[-1][0]:
                min_queue.pop()
            min_queue.append((nums[r], r))
            r += 1
            while max_queue[0][0] - min_queue[0][0] > limit:
                l += 1
                if max_queue[0][1] < l:
                    max_queue.popleft()
                if min_queue[0][1] < l:
                    min_queue.popleft()
            max_len = max(max_len, r - l)
        return max_len
