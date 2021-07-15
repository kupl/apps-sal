import heapq

class Solution:
    
    def calculateSteps(self, num):
        count = 0
        while num > 1:
            if num%2==0:
                num = num//2
            else:
                num = (3*num) + 1
            count+=1
        return count
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        vals = []
        for num in range(lo, hi+1):
            heapq.heappush(vals, (self.calculateSteps(num), num))
        
        print(vals)
        count = 1
        val = None
        while count < k:
            heapq.heappop(vals)
            count+=1
        return heapq.heappop(vals)[1]
            
        

