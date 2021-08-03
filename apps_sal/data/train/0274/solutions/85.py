from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q = deque()
        min_q = deque()

        i = 0
        res = 0
        for j, num in enumerate(nums):
            while max_q and num > max_q[-1]:
                max_q.pop()
            while min_q and num < min_q[-1]:
                min_q.pop()

            max_q.append(num)
            min_q.append(num)

            while max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[i]:
                    max_q.popleft()
                if min_q[0] == nums[i]:
                    min_q.popleft()
                i += 1

            res = max(res, j - i + 1)

        return res
