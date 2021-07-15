from heapq import heappush, heappop
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # min_stack = []
        # max_stack = []
        # for i, number in enumerate(nums):
        #     _index = i
        #     while max_stack and number > max_stack[-1][0]:
        #         _, _index = max_stack.pop()
        #     max_stack.append((number, _index))
        #     _index = i
        #     while min_stack and number < min_stack[-1][0]:
        #         _, _index = min_stack.pop()
        #     min_stack.append((number, _index))
        # longest = -1
        # start_index = len(nums) - 1
        # print(max_stack)
        # print(min_stack)
        # while max_stack[-1][0] - min_stack[-1][0] <= limit:
        #     longest = max(
        #         longest,
        #         abs(max_stack[-1][1] - min_stack[-1][1])
        #     )
        #     if max_stack[-1][1] > min_stack[-1][1]:
        #         max_stack.pop()
        #     else:
        #         min_stack.pop()
        # return longest
            
            
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
                _, _index =min_q.pop()
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
    

