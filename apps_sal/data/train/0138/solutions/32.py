class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        maxl = 0
        pos = 0
        neg = 0
        for n in nums:
            if n == 0:
                pos, neg = 0, 0
            elif n > 0:
                pos += 1
                neg = neg + 1 if neg != 0 else 0
            elif n < 0:
                oldneg = neg
                neg = pos + 1
                pos = oldneg + 1 if oldneg > 0 else 0
            maxl = max(maxl, pos)
        
        return maxl
                

