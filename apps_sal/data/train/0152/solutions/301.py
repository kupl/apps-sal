class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
         
        def helper(position, x, m):
            prev = position[0]
            m -= 1
            #greedy
            for i in range(1, len(position)):
                if position[i] - prev>= x:
                    prev = position[i]
                    m -=1                  
                if m == 0:
                    break            
            if m == 0:
                return x
            else:
                return -1
        
        l = 1
        r = position[-1] - position[0] + 1
        ans = 0
        while l < r:
            mid = (l + r)//2
            realMinimumForce = helper(position, mid, m)
            print((mid, realMinimumForce))
            if realMinimumForce == -1:
                r = mid
            
            else:
                l = mid + 1
                ans = max(ans,realMinimumForce)
                
        
        
        
        return ans

