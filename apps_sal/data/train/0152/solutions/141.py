class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        N = len(position)
        def place(d):
            pre = position[0]
            idx = 1
            for i in range(m-1):
                while idx<N:
                    if position[idx]>=pre+d:
                        break
                    else:
                        idx+=1
                if idx==N:
                    return False
                else:
                    pre = position[idx]
                    
            return True
        
        l = 1
        r = position[-1]-position[0]
        while l<r:
            mid = (l+r+1)//2
            if place(mid):
                l = mid
            else:
                r = mid-1
        return l
