class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l,r = 1, position[-1]
        while l < r:
            mid = ( r + l +1  ) //2 
            cnter = 0
            lst = - (2*mid)
            for i in position:
                if i - lst >=  mid:
                    cnter += 1
                    lst = i 
            if cnter >= m:
                l = mid
            else:
                r = mid -1
        return l

