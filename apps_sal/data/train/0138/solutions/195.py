class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        i = j = 0
        while i < N:
            if nums[i] == 0:
                i += 1
                continue
            j = i
            while j < N and nums[j]:
                j += 1
            negs = 0
            firstneg = lastneg = None
            for k in range(i, j):
                if nums[k] < 0:
                    negs += 1
                    if firstneg is None:
                        firstneg = k
                    lastneg = k
            if negs % 2 == 0:
                ans = max(ans, j - i)
            else:
                ans = max(ans, firstneg - i, j - i - 1 - (firstneg - i))
                ans = max(ans, lastneg - i, j - i - 1 - (lastneg - i))
            i = j
        return ans
