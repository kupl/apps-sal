class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = neg = max_len = 0

        for n in nums:
            if n > 0:
                neg, pos = (1 + neg) if neg > 0 else 0, 1 + pos
                #pos = (1 + pos)
            elif n < 0:
                #n1 = neg
                #neg = (1 + pos)
                pos, neg = (1 + neg) if neg > 0 else 0, 1 + pos

            else:
                pos = neg = 0

            max_len = max(max_len, pos)
        return max_len
