class Solution:
    def numberOfSubarrays(self, A: List[int], k: int) -> int:

        def atMost(k):
            res, lo = 0, 0
            for hi in range(len(A)):
                k -= A[hi] % 2
                while k < 0:
                    k += A[lo] % 2
                    lo += 1
                res += hi - lo + 1
            return res

        return atMost(k) - atMost(k - 1)
