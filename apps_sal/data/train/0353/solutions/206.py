class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        A = sorted(nums)
        r = len(A) - 1
        l = 0
        out = 0
        while l <= r:
            if target - A[r] - A[l] < 0:
                r -= 1
            else:
                out += 2 ** (r - l) % (10 ** 9 + 7)
                l += 1
        return out % (10 ** 9 + 7)
