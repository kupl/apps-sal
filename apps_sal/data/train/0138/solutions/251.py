from typing import List


class Solution:

    def getMaxLen(self, nums: List[int]) -> int:

        def aux(i, j):
            negs = 0
            for v in nums[i:j + 1]:
                if v < 0:
                    negs += 1
            if negs % 2 == 0:
                return j - i + 1
            l = i
            while nums[l] > 0:
                l += 1
            l = j - l
            r = j
            while nums[r] > 0:
                r -= 1
            r = r - i
            return max(l, r)
        start = 0
        maxm = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                maxm = max(maxm, aux(start, end - 1))
                start = end + 1
            elif nums[end] > 0:
                maxm = max(maxm, 1)
        if start != len(nums) - 1:
            maxm = max(maxm, aux(start, len(nums) - 1))
        return maxm
