class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        (r0, r1, r2) = (0, 0, 0)
        for val in nums:
            r = val % 3
            if r == 0:
                new_r0 = r0 + val
                new_r1 = r1 + val if r1 else 0
                new_r2 = r2 + val if r2 else 0
            elif r == 1:
                new_r0 = max(r2 + val, r0) if r2 else r0
                new_r1 = max(r0 + val, r1)
                new_r2 = max(r1 + val, r2) if r1 else r2
            elif r == 2:
                new_r0 = max(r1 + val, r0) if r1 else r0
                new_r1 = max(r2 + val, r1) if r2 else r1
                new_r2 = max(r0 + val, r2)
            (r0, r1, r2) = (new_r0, new_r1, new_r2)
        return r0
