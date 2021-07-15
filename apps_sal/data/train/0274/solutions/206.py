class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque = [nums[0]]
        max_deque = [nums[0]]
        
        max_stretch = 1
        start = 0
        end = 0
        while end < len(nums) - 1:
            end += 1
            
            while len(min_deque) > 0 and nums[end] < min_deque[-1]:
                min_deque.pop()
            min_deque.append(nums[end])
            
            while len(max_deque) > 0 and nums[end] > max_deque[-1]:
                max_deque.pop()
            max_deque.append(nums[end])
            
            while max_deque[0] - min_deque[0] > limit:
                if min_deque[0] == nums[start]:
                    min_deque.pop(0)
                if max_deque[0] == nums[start]:
                    max_deque.pop(0)
                
                start += 1
                
            if end - start + 1 > max_stretch:
                max_stretch = end - start + 1
                
        return max_stretch
        
#         min_heap = [nums[0]]
#         max_heap = [-nums[0]]
        
#         min_removed = {}
#         max_removed = {}
        
#         max_stretch = 1
#         start = 0
#         end = 0
#         while end < len(nums) - 1:
#             end += 1
#             heapq.heappush(min_heap, nums[end])
#             heapq.heappush(max_heap, -nums[end])
            
#             while - max_heap[0] - min_heap[0] > limit:
#                 if nums[start] not in min_removed:
#                     min_removed[nums[start]] = 0
#                 min_removed[nums[start]] += 1
                
#                 if nums[start] not in max_removed:
#                     max_removed[nums[start]] = 0
#                 max_removed[nums[start]] += 1
                
#                 while -max_heap[0] in max_removed and max_removed[-max_heap[0]] > 0:
#                     max_removed[-max_heap[0]] -= 1
#                     heapq.heappop(max_heap)
                    
#                 while min_heap[0] in min_removed and min_removed[min_heap[0]] > 0:
#                     min_removed[min_heap[0]] -= 1
#                     heapq.heappop(min_heap)
                    
#                 start += 1
                
#             if end - start + 1 > max_stretch:
#                 max_stretch = end - start + 1
                
#         return max_stretch

