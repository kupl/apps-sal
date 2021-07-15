class Solution:
     def findKthLargest(self, nums, k):
         """
         :type nums: List[int]
         :type k: int
         :rtype: int
         """
         if not nums: return -1;
         pq = [];
 
         for num in nums:
             if len(pq) < k:
                 heapq.heappush(pq,num);
             else:
                 popped = heapq.heappop(pq);
                 if popped < num:
                     heapq.heappush(pq, num);
                 else:
                     heapq.heappush(pq, popped);
 
         return heapq.heappop(pq);        
