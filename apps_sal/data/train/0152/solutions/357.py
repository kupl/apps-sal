class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position = sorted(position)
        i,j = 1,1000000001
        ans = 0 
        while i<=j :
            prevCow = position[0] 
            mid = (i+j)//2 
            currCows = 1 
            for k in range(1,len(position)) : 
                if position[k] - prevCow >= mid : 
                    currCows += 1 
                    prevCow = position[k]
            if currCows < m :
                j = mid - 1
            else :
                i = mid + 1 
                ans = mid 
        return ans 
