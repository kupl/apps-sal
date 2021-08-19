class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_length = 0

        idx = 0
        prev = 0
        negative = 0
        while idx < len(nums):
            num = nums[idx]
            if num == 0:
                prev = 0
                negative = 0
            elif num < 0:
                if negative == 1:
                    prev = neg_idx + (idx - prev_neg_idx) + 1
                    negative = 0
                else:
                    prev_neg_idx = idx
                    neg_idx = prev
                    negative = 1
            else:
                if prev == 0 or negative == 0:
                    prev += 1
            # print(prev)
            max_length = max(max_length, prev)
            idx += 1

        idx = len(nums) - 1
        prev = 0
        negative = 0
        while idx >= 0:
            num = nums[idx]
            if num == 0:
                prev = 0
                negative = 0
            elif num < 0:
                if negative == 1:
                    prev = neg_idx + (prev_neg_idx - idx) + 1
                    negative = 0
                else:
                    prev_neg_idx = idx
                    neg_idx = prev
                    negative = 1
            else:
                if prev == 0 or negative == 0:
                    prev += 1
            # print(prev)
            max_length = max(max_length, prev)
            idx -= 1

        return max_length
