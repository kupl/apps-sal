from collections import deque
class Solution: #revisit 09/09/2020
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # for a window, find the window max and the window min
        # left and right pointer
        # use max_queue and min_queue to calculate the window max and window min
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
                
# e.g. [10,1,2,4,7,2], limit = 5
# left, right =2,5, min_q = [(5,2)], max_q = [(4,7), (5,2)] max_lenght = 4











# from collections import deque
# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:
#         N = len(nums)
#         if N == 1:
#             return 1
        
#         result = 0
#         min_q, max_q = deque([]), deque([])
#         l, r = 0, 0
#         while r < N:
#             while min_q and nums[min_q[-1]] >= nums[r]:
#                 min_q.pop()
#             while max_q and nums[max_q[-1]] <= nums[r]:
#                 max_q.pop()
#             min_q.append(r)
#             max_q.append(r)
            
#             while nums[max_q[0]] - nums[min_q[0]] > limit:
#                 l += 1
#                 if max_q[0] < l:
#                     max_q.popleft()
#                 if min_q[0] < l:
#                     min_q.popleft()
                    
#             #print(f\"l = {l}, r = {r}, min_q = {min_q}, max_q = {max_q}\")
#             result = max(result, r - l + 1) 
#             r += 1
#         return result
        

