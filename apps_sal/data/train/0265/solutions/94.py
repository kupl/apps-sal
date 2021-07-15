class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        sett = set([0])
        ans = 0
        cur = 0
        for val in nums:
            cur += val
            if cur - target in sett:
                ans += 1
                sett = set()
            sett.add(cur)
        return ans
