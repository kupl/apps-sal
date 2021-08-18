from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        N = len(nums)
        max_q, min_q = deque([]), deque([])
        left, right = 0, 0
        max_length = 0
        while right < N:
            while max_q and max_q[-1][1] <= nums[right]:
                max_q.pop()
            max_q.append([right, nums[right]])
            while min_q and min_q[-1][1] >= nums[right]:
                min_q.pop()
            min_q.append([right, nums[right]])

            while max_q[0][1] - min_q[0][1] > limit:
                left += 1
                if max_q[0][0] < left:
                    max_q.popleft()
                if min_q[0][0] < left:
                    min_q.popleft()

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length
