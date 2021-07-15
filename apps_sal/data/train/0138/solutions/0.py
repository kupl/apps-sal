class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        maxx = 0
        nums.append(0)
        
        # starting position
        # where we find a 0
        i = -1
        minusarr = []
        
        for j,n in enumerate(nums):
            if n == 0:
                # now figure out previous ones
                tot = j-i-1
                if not minusarr or len(minusarr)%2 == 0:
                    maxx = max(maxx, tot)
                else:
                    # drop the first or last 0
                    left = minusarr[0]-i
                    right = j-minusarr[-1]
                    maxx = max(maxx, tot - min(left, right))
                
                # reinitiate
                minusarr = []
                i = j
            elif n < 0:
                minusarr.append(j)
        return maxx
