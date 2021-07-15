class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_pos = 0
        max_neg = 0
        max_len = 0
        for n in nums:
            if n == 0:
                max_pos = max_neg = 0
            elif n > 0:
                max_pos += 1
                if max_neg:
                    max_neg += 1
            else:
                prev_pos = max_pos
                if max_neg:
                    max_pos = max_neg + 1
                else:
                    max_pos = 0
                max_neg = prev_pos + 1
            max_len = max(max_len, max_pos)
        return max_len
