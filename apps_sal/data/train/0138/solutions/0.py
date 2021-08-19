class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        maxx = 0
        nums.append(0)
        i = -1
        minusarr = []
        for (j, n) in enumerate(nums):
            if n == 0:
                tot = j - i - 1
                if not minusarr or len(minusarr) % 2 == 0:
                    maxx = max(maxx, tot)
                else:
                    left = minusarr[0] - i
                    right = j - minusarr[-1]
                    maxx = max(maxx, tot - min(left, right))
                minusarr = []
                i = j
            elif n < 0:
                minusarr.append(j)
        return maxx
