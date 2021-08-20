class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        seen = set()
        seen.add(0)
        curr = 0
        res = 0
        for n in nums:
            curr += n
            if curr - target in seen:
                res += 1
                curr = 0
                seen = set([0])
            else:
                seen.add(curr)
        return res
