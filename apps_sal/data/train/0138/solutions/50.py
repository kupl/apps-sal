class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos_l = 0
        neg_l = 0
        best = 0

        for n in nums:
            if n == 0:
                pos_l = 0
                neg_l = 0
            elif n > 0:
                pos_l += 1
                if neg_l > 0:
                    neg_l += 1
            else:
                if neg_l == 0 and pos_l == 0:
                    neg_l = 1
                elif neg_l > 0 and pos_l > 0:
                    pos_l, neg_l = neg_l + 1, pos_l + 1
                elif neg_l > 0:
                    pos_l = neg_l + 1
                    neg_l = 1
                elif pos_l > 0:
                    neg_l = pos_l + 1
                    pos_l = 0
            best = max(best, pos_l)
        return best
