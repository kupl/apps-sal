class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        seen = set([0])

        out = 0

        curr = 0

        for i in nums:
            curr += i
            if curr - target in seen:
                out += 1
                seen = set([0])
                curr = 0
            else:
                seen.add(curr)

        return out
