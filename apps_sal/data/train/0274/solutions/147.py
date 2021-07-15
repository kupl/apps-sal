#TRY 8/19/2020 
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = collections.deque()
        min_deque = collections.deque()
        
        start = 0
        end = 0 
        max_limit_subarray = 0
        for end in range(len(nums)): 
            while min_deque and nums[end] < nums[min_deque[-1]]: 
                min_deque.pop()
            min_deque.append(end)
            
            while max_deque and nums[end] > nums[max_deque[-1]]: 
                max_deque.pop()
                
            max_deque.append(end)
            
            # max_val = nums[max_deque[0]]
            # min_val = nums[min_deque[0]]
            # limit_break = abs(max_val - min_val)
            while abs(nums[max_deque[0]] - nums[min_deque[0]]) > limit: #limit has been broken. 
#                 limit_break -= nums[start]
                start += 1 #shrink the window.
                if start > min_deque[0]: 
                    min_deque.popleft()
                if start > max_deque[0]:
                    max_deque.popleft()
                
             
            
            #Get the best window length so far.        
            max_limit_subarray = max(max_limit_subarray, end - start + 1)
            
        return max_limit_subarray
                
            
            
            
# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:
#         # sanity check
#         if nums is None or len(nums) <= 1 or limit < 0:
#             return 1
        
#         # sliding window approach in O(n) time
#         max_len, l, r = 0, 0, 0
        
#         # notice that, the only absolute difference we need to check is the 
#         # maximum possible absolute difference since it ensures there are no
#         # other absolute differences that can be bigger than @limit
#         max_val, min_val = 0, 0
        
#         # dequeu method of keeping a local min and max over a sliding window in 
#         # amortized O(1) time 
#         # reference: https://www.nayuki.io/page/sliding-window-minimum-maximum-algorithm
#         min_dq, max_dq = [], []
        
#         while r < len(nums):
#             val = nums[r] 
            
#             # update min_dq
#             while len(min_dq) > 0 and val < min_dq[-1]:
#                 min_dq.pop()
#             min_dq.append(val)
            
#             # update max_dq
#             while len(max_dq) > 0 and val > max_dq[-1]:
#                 max_dq.pop()
#             max_dq.append(val)

#             max_val = max_dq[0]
#             min_val = min_dq[0]
            
#             diff = abs(max_val - min_val)
            
#             # note that we do not have to worry about the left pointer passing the right one
#             if diff > limit:
#                 # recalculate min and max values of window by updating dequeues
#                 check = nums[l]
#                 if check == min_dq[0]:
#                     min_dq.pop(0)
#                 if check == max_dq[0]:
#                     max_dq.pop(0)
                
#                 # shrink window
#                 l += 1
            
#             # expand window
#             max_len = max(max_len, r - l + 1)
#             r += 1
        
#         return max_len  


# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:
#         #int array nums
#         #int limit 
#         #ret longest non-empty subarray s.t 
#         #the absolute diff betweeen any two elemetns of the subarray is <= limit 
        
#         start = 0
#         end = 0 
        
#         min_ele = float('inf')
#         max_ele = float('-inf')
#         sub_array = []
        
#         contig_sub = float('-inf')
#         #currently start at zero but let's see if we can try to start at the end maybe? 
#         while end < len(nums):
#             sub_array = nums[start:end + 1]
#             limit_breaker = abs(max(sub_array) - min(sub_array))
            
#             while limit_breaker > limit: #You are too much :'( 
#                 tmp = start 
            
#                 limit_breaker -= nums[tmp]
#                 # start += 1 #This is too early because once we've subtracted we're using it 
#                 #This means that start wil lbe < 1 for contig sub potentially. 
                
#             if limit_breaker <= limit: #You are okay. 
#                 contig_sub = max(contig_sub, end - start + 1)
#             end += 1
        
#         return contig_sub

# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:
#         #Queues to take the min and the max of our subarray so far.
#         min_deque, max_deque = deque(), deque()
#         l = r = 0
#         ans = 0
#         while r < len(nums):
#             #Min_deque has the minimum value position and check if there are better ones 
#             while min_deque and nums[r] <= nums[min_deque[-1]]:
#                 min_deque.pop()
#             min_deque.append(r)
            
#             #Max_deque has the maximum value position and check if there are better ones 
#             while max_deque and nums[r] >= nums[max_deque[-1]]:
#                 max_deque.pop()
#             max_deque.append(r)
            
#             #Limit break the limit? 
#             #If it does then we can find the next one. 
#             while nums[max_deque[0]] - nums[min_deque[0]] > limit:
#                 l += 1
#                 #if the next position is > than our current one than we know it's no longer a part of the subarray.
#                 if l > min_deque[0]:
#                     min_deque.popleft()
#                 if l > max_deque[0]:
#                     max_deque.popleft()
            
#             ans = max(ans, r - l + 1)
#             r += 1
                
#         return ans
                         

