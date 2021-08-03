class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        neg = pos = max_len = 0
        fneg = lneg = -1
        beg = -1

        for i, n in enumerate(nums):
            if n < 0:
                neg += 1
                if fneg == -1:
                    fneg = lneg = i
                else:
                    lneg = i
            elif n > 0:
                pos += 1
            else:
                if neg % 2 == 0:
                    max_len = max(max_len, neg + pos)
                else:
                    max_len = max(max_len, max(lneg - beg - 1, i - fneg - 1))
                    print((i, fneg, lneg, beg))
                neg = pos = 0
                fneg = lneg = -1
                beg = i

        if neg % 2 == 0:
            max_len = max(max_len, neg + pos)
        else:
            max_len = max(max_len, max(i - fneg, lneg - beg - 1))

        return max_len
