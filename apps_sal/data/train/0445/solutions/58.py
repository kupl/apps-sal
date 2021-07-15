import heapq
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) <= 4:
            return 0
        
        minheap = []
        maxheap = []
        
        for j, num in enumerate(nums):
            
            if len(minheap) < 4:
                heapq.heappush(minheap, -num)
            else:
                x = heapq.heappop(minheap)
                if x > -num:
                    heapq.heappush(minheap, x)
                else:
                    heapq.heappush(minheap, -num)
                    
            if len(maxheap) < 4:
                heapq.heappush(maxheap, num)
            else:
                x = heapq.heappop(maxheap)
                if x > num:
                    heapq.heappush(maxheap, x)
                else:
                    heapq.heappush(maxheap, num)
        
        minheap = [-x for x in minheap]
        minheap.sort()
        maxheap.sort()
        
        diff = [maxheap[-1]-minheap[-1], 
                maxheap[0]-minheap[0],
                maxheap[-2]-minheap[2],
                maxheap[-3]-minheap[1]]
        
        return min(diff)
                

