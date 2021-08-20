class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1 if nums[0] > 0 else 0

        def find(start, end):
            if start + 1 == end:
                return 0
            neg_count = sum((1 for x in range(start + 1, end) if nums[x] < 0))
            if neg_count % 2 == 0:
                return end - start + 1 - 2
            (first_neg, last_neg) = (None, None)
            for idx in range(start + 1, end):
                if nums[idx] < 0:
                    if first_neg is None:
                        first_neg = idx
                    last_neg = idx
            return max(last_neg - 1 - (start + 1) + 1, end - 1 - (first_neg + 1) + 1)
        (NEG, POS, ZERO) = (-1, +1, 0)
        nums = [0] + nums + [0]
        n = len(nums)
        start = 0
        end = 1
        ans = 0
        while end < n:
            while end < n and nums[end] != 0:
                end += 1
            ans = max(ans, find(start, end))
            start = end
            end += 1
        return ans
