class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        out = 0
        first = -1
        last = -1
        negs = 0
        start = 0
        for i, num in enumerate(nums):
            if num == 0:
                if negs % 2 == 0:
                    new_max = i - start
                else:
                    new_max = max(i - first - 1, last - start)
                out = max(out, new_max)
                first = -1
                last = -1
                negs = 0
                start = i + 1
            if num < 0:
                negs += 1
                if first == -1:
                    first = i
                last = i
        i += 1
        if negs % 2 == 0:
            new_max = i - start
        else:
            new_max = max(i - first - 1, last - start)
        out = max(out, new_max)
        return out
