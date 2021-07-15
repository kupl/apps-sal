class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        min_heap = []
        max_heap = []
        longest_window = 1
        
        min_idx = 0
        for i, num in enumerate(nums):
            
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            # print(min_heap)
            # print(max_heap)
            # print(min_heap[0][0], max_heap[0][0])
            
            while min_heap[0][1] < min_idx:
                heapq.heappop(min_heap)
            while max_heap[0][1] < min_idx:
                heapq.heappop(max_heap)
            if abs(min_heap[0][0] + max_heap[0][0]) > limit:
                #print('here')
                if (min_heap[0][1] < max_heap[0][1]):
                    min_idx = min_heap[0][1] + 1
                    heapq.heappop(min_heap)
                    #print('min_idx', min_idx)
                else:
                    min_idx = max_heap[0][1] + 1
                    heapq.heappop(max_heap)
                    
            #print(min_heap[0][1], max_heap[0][1])
            #print(min_idx, i)
            longest_window = max(longest_window, i - min_idx + 1)
                                 
                                 
        return longest_window
            

