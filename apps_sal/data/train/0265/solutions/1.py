class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        res = 0
        s = set()
        s.add(0)
        t = 0
        for x in nums:
            t += x
            if t - target in s:
                res += 1
                s.clear()
            s.add(t)
        return res
