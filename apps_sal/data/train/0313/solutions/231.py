class Solution:
    def minDays(self, A: List[int], m: int, k: int) -> int:
        if m * k > len(A):
            return -1
        
        def isit(d):
            c = b = 0
            for a in A:
                c = 0 if a>d else c+1
                if c==k:
                    c=0
                    b+=1
                    if b==m:
                        return 1
            return 0

        l = 1
        r = max(A)
        while l < r:
            mid = (l+r)//2
            if isit(mid):
                r = mid
            else:
                l = mid + 1
        return l

