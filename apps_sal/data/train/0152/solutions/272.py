class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l, r, sol = 0, position[-1] - position[0], -1
        
        def helper(target):
            pre, cnt = position[0], 1
            
            for n in position:
                temp = n - pre
                
                if temp >= target: 
                    cnt += 1
                    pre = n                    
                                                            
            if (position[-1] - pre) >= target: cnt += 1
                
            if cnt >= m: return True
            
            return False
            
        while l <= r:
            mid = (l + r) // 2
            
            if (helper(mid)):
                l = mid + 1
                
            else:
                r = mid - 1
                
        return l - 1
            
            
                

