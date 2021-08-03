class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = int(nums[0] > 0)
        neg = int(nums[0] < 0)
        best = pos
        for i in nums[1:]:
            if i > 0:
                pos += 1
                if neg > 0:
                    neg += 1
                else:
                    neg = 0
            elif i < 0:
                pTemp = pos
                if neg > 0:
                    pos = neg + 1
                else:
                    pos = 0
                neg = pTemp + 1
            else:
                pos, neg = 0, 0
            best = max(best, pos)
        return best
