class Solution:
    def numSubseq(self, A: List[int], target: int) -> int:
        A.sort()
        l, r = 0, len(A) - 1
        res = 0
        mod = 10**9 + 7
        while l <= r:
            if A[l] + A[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, mod)  # For each elements in the subarray A[i+1] ~ A[j],we can pick or not pick
                l += 1
        return res % mod
