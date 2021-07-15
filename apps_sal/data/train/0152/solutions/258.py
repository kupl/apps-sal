class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        high=position[-1]-position[0]
        low = high
        for i in range(1, len(position)):
            low = min(low, position[i]-position[i-1])
        
        def feasible(force):
            last = position[0]
            count=1
            for i in range(1,len(position)):
                if (position[i]-last)>=force:
                    last=position[i]
                    count+=1
            if count >= m:
                return True
            return False
        
        while low < high:
            mid = (low+high)//2
            if not feasible(mid):
                high=mid
            else:
                low=mid+1
        low-=1
        ans=float('inf')
        last=position[0]
        for i in range(1, len(position)):
            if (position[i]-last)>=low:
                ans=min(ans, position[i]-last)
                last=position[i]
        
        return ans
        

