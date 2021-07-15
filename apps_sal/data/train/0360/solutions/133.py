class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def canDo(k):
            d = 1
            curr = 0
            for w in weights:
                if w > k:
                    return False
                curr += w
                if curr > k:
                    d +=1
                    curr = w
            return d <= D
        
        l,r = 0,10**18
        while l < r:
            m = (l+r)//2
            # print(l,r,m,canDo(m))
            if canDo(m):
                r = m
            else:
                l = m+1
        return l
                
                

