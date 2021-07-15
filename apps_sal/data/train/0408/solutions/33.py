class Solution:
    
    def delta (self, val: int,arr: List[int], target: int) -> int:
            total = 0 
            
            for a in arr:
                if (a < val):
                    total += a 
                else:
                    total += val
            
            return (abs(total-target))
        
        
            
    def check(self, val: int,arr: List[int], target: int) -> bool:
            
            if ((self.delta(val, arr, target)-self.delta(val+1, arr, target))<=0):
                return True
            else: 
                return False
            
            
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        lo = 0
        hi= sum(arr)
        
        while(lo<hi):
            
            mid = lo +((hi-lo)//2)  
                
            if (self.check(mid, arr, target)):
                hi = mid 
            else: 
                lo = mid +1
            
        
        if (self.check(lo, arr, target)):
                return lo 
        else : 
            return (0)
