class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        pos_length = 0
        neg_length = 0
        max_length = 0
        for num in nums:
            if num > 0:
                pos_length += 1
                if neg_length:
                    neg_length += 1
            elif num < 0:
                tmp = pos_length
                if neg_length:
                    pos_length = neg_length + 1
                else:
                    pos_length = 0
                neg_length = tmp + 1
            else:
                pos_length = 0
                neg_length = 0
            max_length = max(max_length, pos_length)
        max_length = max(max_length, pos_length)
        return max_length
