class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = 1
        r = 1000000000
        if m * k > len(bloomDay):
            return -1
        
        while l < r:
            
            mid = l + (r - l)//2
            if self.validflower(mid, bloomDay, k, m) == True:
                r = mid
            else:
                l = mid + 1
        return l         
            
 
            
    def validflower(self, mid, bloomDay, k, m):
        count = 0
        f = 0
        for j in bloomDay:
            if j <= mid:
                f += 1
            else:
                f = 0
                
            if f == k:
                count += 1
                f = 0
            
        if count >= m:
            return True
        
        return False
                

