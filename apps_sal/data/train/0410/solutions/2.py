from heapq import heappush, heappop

class Solution:
    dp = {}
    
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        heap = []
        
        for i in range(lo, hi+1):
            heappush(heap, [self.getPower(i), i])
        
        if len(heap) < k:
            return -1
        
        result = heappop(heap)
        for i in range(1, k):
            result = heappop(heap)
            
        return result[1]
        
        
        
    def getPower(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n in self.dp:
            return self.dp[n]
        
        result = 0
        
        if n % 2 == 0:
            result = 1 + self.getPower(n // 2)
        else:
            result = 1 + self.getPower(n * 3 + 1)
            
        self.dp[n] = result
        return result
