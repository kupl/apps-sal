class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        ans = pos = neg = 0
        for x in nums:
            if x > 0:
                (pos, neg) = (1 + pos, 1 + neg if neg else 0)
            elif x < 0:
                (pos, neg) = (1 + neg if neg else 0, 1 + pos)
            else:
                pos = neg = 0
            ans = max(ans, pos)
        return ans
