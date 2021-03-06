"""class Solution:
    def numSubseq(self, A: List[int], target: int) -> int:
        A.sort()
        l, r = 0, len(A) - 1
        res = 0
        mod = 10**9 + 7
        while l <= r:
            if A[l] + A[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, mod)
                l += 1
        return res % mod"""


class Solution:

    def numSubseq(self, A, target):
        A.sort()
        l = 0
        r = len(A) - 1
        res = 0
        mod = 10 ** 9 + 7
        while l <= r:
            if A[l] + A[r] <= target:
                res += pow(2, r - l, mod)
                l += 1
            else:
                r -= 1
        return res % mod
