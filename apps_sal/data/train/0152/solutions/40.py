class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        s = 1 
        e = (position[-1]-position[0]) // max(m-1, 1) + 1
        
        def check(mid) :
            t = position[0]
            ret_val = 1
            for k in position :
                if ret_val == m :
                    return True
                if k - t >= mid :
                    ret_val += 1
                    t = k
            return ret_val == m
        
        while e > s + 1 :
            mid = (e+s)//2
            if check(mid) :
                s = mid
            else :
                e = mid
        return s
        
        

