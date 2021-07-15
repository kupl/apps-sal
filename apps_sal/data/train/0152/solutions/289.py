class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        lo=0   
        hi=position[-1]-position[0]
        n=len(position)
        
        def count(d):
            ans, curr = 1, position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    ans += 1
                    curr = position[i]
            return ans
                    
            
        while lo<hi:
            mid= (lo+hi+1)//2
            res=count(mid)
            if res>=m:
                lo=mid
            elif res<m:
                hi=mid-1
        return lo
            

