class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:

        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)
        res = 0
        seen = set()
        for x in prefix:
            if x - target in seen:
                res += 1
                seen = {x}
            else:
                seen.add(x)
        return res
