class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        zero = one = two = 0
        for n in nums:
            nz, no, nt = zero + n, one + n, two + n
            zero = max(zero, nz if nz % 3 == 0 else 0, no if no % 3 == 0 else 0, nt if nt % 3 == 0 else 0)
            one = max(one, nz if nz % 3 == 1 else 0, no if no % 3 == 1 else 0, nt if nt % 3 == 1 else 0)
            two = max(two, nz if nz % 3 == 2 else 0, no if no % 3 == 2 else 0, nt if nt % 3 == 2 else 0)

        return zero
