class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        (res, sm) = (0, 0)
        hs = set()
        hs.add(0)
        for v in nums:
            sm += v
            if sm - target in hs:
                res += 1
                sm = 0
                hs.clear()
                hs.add(0)
            else:
                hs.add(sm)
        return res
