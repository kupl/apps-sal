from heapq import heappush, heappop
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        left = 0
        min_q = deque()
        max_q = deque()
        longest = 0
        for right, number in enumerate(nums):
            _index = right
            while max_q and number > max_q[-1][0]:
                _, _index = max_q.pop()
            max_q.append((number, _index))
            _index = right
            while min_q and number <= min_q[-1][0]:
                _, _index = min_q.pop()
            min_q.append((number, _index))
            while max_q[0][0] - min_q[0][0] > limit:
                if max_q[0][1] > min_q[0][1]:
                    if len(min_q) == 1:
                        q = max_q
                    else:
                        q = min_q
                else:
                    if len(max_q) == 1:
                        q = min_q
                    else:
                        q = max_q
                _, _index = q.popleft()
            left = max(min_q[0][1], max_q[0][1])
            longest = max(longest, right - left + 1)
        return longest

    def calc_diff(self, a, b):
        return abs(a - b)
