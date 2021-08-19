class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = pos = neg = 0
        for x in nums:
            if x > 0:
                pos, neg = 1 + pos, 1 + neg if neg else 0     # assignment in one line is very important to have the previous value of variables updated! Cannot be re-written into 2 lines!
            elif x < 0:
                pos, neg = 1 + neg if neg else 0, 1 + pos
            else:
                pos = neg = 0  # reset
            ans = max(ans, pos)
        return ans
