class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        
        def count(d):
            ans = 1
            pos = position[0]
            for i in range(1,n):
                if position[i]-pos>=d:
                    ans+=1
                    pos = position[i]
            return ans
        
        l = 0
        r = position[-1] - position[0]
        
        while l<r:
            mid = (l+r+1)//2
            
            if count(mid)>=m: 
                l = mid
            else:
                r = mid-1
        
        return l        
