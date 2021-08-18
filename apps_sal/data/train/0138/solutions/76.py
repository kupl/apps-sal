class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res = 0
        pos, neg = set(), set()
        for num in nums:
            if num > 0:
                pos = {x + 1 for x in pos} | {1}
                neg = {y + 1 for y in neg}
            elif num < 0:
                pos = {x + 1 for x in pos} | {1}
                neg = {y + 1 for y in neg}
                pos, neg = neg, pos
            else:
                pos, neg = set(), set()

            if len(pos):
                res = max(res, max(pos))

            if len(pos):
                pos = set([max(pos)])
            if len(neg):
                neg = set([max(neg)])
        return res
