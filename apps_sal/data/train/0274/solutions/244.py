class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque

        min_q = deque()
        max_q = deque()
        ans = 0
        j = 0
        for i, num in enumerate(nums):
            while min_q and min_q[-1][0] > num:
                min_q.pop()
            min_q.append((num, i))
            while max_q and max_q[-1][0] < num:
                max_q.pop()
            max_q.append((num, i))
            if abs(min_q[0][0] - max_q[0][0]) <= limit:
                ans = max(ans, i - j + 1)
            else:
                if min_q[0][1] < max_q[0][1]:
                    j = min_q[0][1] + 1
                    min_q.popleft()
                elif min_q[0][1] > max_q[0][1]:
                    j = max_q[0][1] + 1
                    max_q.popleft()
                else:
                    j = max_q[0][1] + 1
                    min_q.popleft()
                    max_q.popleft()
        return ans
