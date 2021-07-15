class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # binary search
        def isValid(f, k):
            # return true if it is possible to arrange m elements in array such that minimum distance is f
            pos = position[0]
            count = 1
            for i in range(1, n):
                if (position[i] - pos >= f):
                    # put it here
                    pos = position[i]
                    count += 1
                    
                    if count == k:
                        return True
                    
            return False
        
        n = len(position)
        position.sort()
        res = 0
        
        l, r = 0, position[n-1] - position[0] + 1
        while l < r:
            mid = (l+r) >> 1
            if isValid(mid, m):
                res = max(res, mid)
                l = mid + 1
                
            else:
                r = mid
                
        return res
