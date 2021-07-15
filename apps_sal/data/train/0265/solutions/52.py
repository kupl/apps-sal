class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        tot = 0
        seen = set([0])
        cur = 0
        for n in nums:
            cur += n
            if cur - target in seen:
                tot += 1
                cur = 0
                seen = set([0])
            else:
                seen.add(cur)
        return tot

