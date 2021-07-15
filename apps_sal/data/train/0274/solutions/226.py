import heapq
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        minheap=[]
        maxheap=[]
        heapq.heapify(minheap)
        heapq.heapify(maxheap)
        
        heapq.heappush(minheap,[nums[0],0]) # add first element and its index
        heapq.heappush(maxheap,[-nums[0],0])

        
        begin = 0
        length = 1        
        end = 1
        next_idx = 0
        while begin <= end and end <= len(nums) - 1:
            
            if abs(minheap[0][0] - nums[end]) <= limit and abs(abs(maxheap[0][0]) - nums[end]) <= limit:
                length = max(length, (end - begin) + 1)

            else:
                while len(minheap) > 0 and abs(minheap[0][0] - nums[end]) > limit:
                    ele,idx = heapq.heappop(minheap)
                    next_idx = max(next_idx, idx)
                while len(maxheap) > 0 and abs(-maxheap[0][0] - nums[end]) > limit:
                    ele,idx = heapq.heappop(maxheap)
                    next_idx = max(next_idx, idx)
                begin = next_idx + 1 
            heapq.heappush(minheap, [nums[end],end])
            heapq.heappush(maxheap, [-nums[end],end])
            end+=1
        return length
        
#         minheap=[]
#         maxheap=[]
#         heapq.heapify(minheap)
#         heapq.heapify(maxheap)
#         length=1
#         i=0
#         j=1
#         heapq.heappush(minheap,[nums[0],0]) # add first element and its index
#         heapq.heappush(maxheap,[-nums[0],0])
#         maxindex=0
#         while i<=j and j<=len(nums)-1:
#             if abs(minheap[0][0]-nums[j])<=limit and abs(abs(maxheap[0][0])-nums[j])<= limit:
#                 length=max(length,j-i+1)
                
#             else:
#                 while len(minheap)>0 and abs(minheap[0][0]-nums[j])>limit:
#                     ele,index=heapq.heappop(minheap)
#                     maxindex=max(maxindex,index)
#                 while len(maxheap)>0 and abs(-maxheap[0][0]-nums[j])>limit:
#                     ele,index=heapq.heappop(maxheap)
#                     maxindex=max(maxindex,index)
#                 i=maxindex+1   # update i and now  we are not concerned with element before ith index
#             heapq.heappush(minheap,[nums[j],j]) # add  element and its index
#             heapq.heappush(maxheap,[-nums[j],j])
#             j=j+1
            
#         return length
        
#         def isValid(int_diff, j, max_value, min_value, limit, nums):
#             max_boundary = abs(max_value - nums[j])
#             min_boundary = abs(min_value - nums[j])
#             return int_diff <= limit and max_boundary <= limit and min_boundary <= limit
        
#         def find_error(int_diff,i, j, max_value, min_value, limit, nums,cache):
#             max_boundary = abs(max_value - nums[j])
#             min_boundary = abs(min_value - nums[j])
            
#             if int_diff > limit: return i
#             if max_boundary > limit: return cache[max_value]
#             if min_boundary > limit: return cache[min_value]
            
#         output = 1
#         i = 0
#         idx = 0
#         cache = defaultdict(int)
#         while i < len(nums) and idx < len(nums)-1:
#             min_value = float('inf')
#             max_value = float('-inf')
#             cache[min_value] = i
#             cache[max_value] = i
#             for j in range(i,len(nums)):
                
#                 int_diff = abs(nums[j] - nums[i])
#                 temp_min = min_value
#                 temp_max = max_value
#                 min_value = min(min_value, nums[j])
#                 max_value = max(max_value, nums[j])
#                 if temp_min != min_value:
#                     cache[min_value] = j
#                 if temp_max != min_value:
#                     cache[max_value] = j
#                 if isValid(int_diff, j, max_value, min_value, limit, nums):
#                     output = max(output, (j - i) + 1)
#                 else:
#                     i = find_error(int_diff, i, j, max_value, min_value, limit, nums,cache) + 1
                    
#                     break
#                 idx = j
#         return output
                
                
        
            

