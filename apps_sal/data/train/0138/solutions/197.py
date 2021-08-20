class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        first_neg = -1
        last_neg = -1
        pos = True
        start = 0
        best = 0
        n = len(nums)
        for (i, num) in enumerate(nums):
            if num == 0:
                if pos:
                    best = max(best, i - start)
                elif first_neg >= start:
                    best = max(best, i - first_neg - 1, last_neg - start)
                start = i + 1
                pos = True
            elif num < 0:
                last_neg = i
                if first_neg < start:
                    first_neg = i
                pos = not pos
        if pos:
            best = max(best, n - start)
        elif first_neg >= start:
            best = max(best, n - first_neg - 1, last_neg - start)
        return best
