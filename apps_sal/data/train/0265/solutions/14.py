class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        res = 0
        csum = [0]
        for n in nums:
            csum.append(csum[-1] + n)
        seen = set([])
        for c in csum[:]:
            if c - target in seen:
                res += 1
                seen.clear()
            seen.add(c)

        return res
