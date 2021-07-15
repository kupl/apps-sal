import math
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        diff = []
        for i in range(n-1):
            diff.append(position[i+1]-position[i])
        
        def check(force,diff,num):
            i = 0
            j = 0
            curr = 0
            while i < len(diff):
                curr += diff[i]
                if curr >= force:
                    j += 1
                    curr = 0
                i += 1
            return j >= num
        
        if m == 2:
            return position[n-1]-position[0]
        
        start = 1
        end = math.ceil((position[n-1]-position[0])/(m-1))
        mid = (start+end)//2
        ansList = []
        while start < end:
            if check(mid,diff,m-1):
                start = mid+1
                ansList.append(mid)
            else:
                end = mid-1
            mid = (start+end)//2
        if check(mid,diff,m-1):
            ansList.append(mid)
        return max(ansList)
                


