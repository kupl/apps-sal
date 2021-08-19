class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        d = {0: -1}
        cursum = 0
        ans = 0
        for (i, n) in enumerate(nums):
            cursum += n
            prev = cursum - target
            if prev in d:
                ans += 1
                d = {}
            d[cursum] = i
        return ans
