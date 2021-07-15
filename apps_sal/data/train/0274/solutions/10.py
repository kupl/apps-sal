class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        minHeap =  []
        maxHeap = []
        
        l = 0 
        
        maxSize = 0 
        
        for r,num in enumerate(nums):
            heappush(minHeap, (num, r))
            heappush(maxHeap, (-num, r))
            
            minElement, minIndex = minHeap[0]
            maxElement, maxIndex = maxHeap[0]
            
            maxElement = -maxElement 
            
            while maxElement - minElement > limit: 
                l+=1
                
                while minHeap[0][1] < l:
                    heappop(minHeap)
                    
                while maxHeap[0][1] < l:
                    heappop(maxHeap)
                    
                minElement, minIndex = minHeap[0]
                maxElement, maxIndex = maxHeap[0]
                
                maxElement = -maxElement 
                
            curSize = r-l+1
            
            maxSize = max(curSize, maxSize)
            
        return maxSize 
