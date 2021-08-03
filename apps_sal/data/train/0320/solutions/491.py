class Solution:
    def minOperations(self, nums: List[int]) -> int:
        shifts = 0
        adds = 0
        for n in nums:
            if n == 0:
                continue
            b = bin(n)[2:]
            shifts = max(shifts, len(b) - 1)
            adds += sum(c == '1' for c in b)
        return shifts + adds
