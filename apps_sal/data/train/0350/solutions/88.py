class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        def atMost(K):
            (res, lo, seen) = (0, 0, Counter())
            for hi in range(len(A)):
                if seen[A[hi]] == 0:
                    K -= 1
                seen[A[hi]] += 1
                while K < 0:
                    seen[A[lo]] -= 1
                    if seen[A[lo]] == 0:
                        K += 1
                    lo += 1
                res += hi - lo + 1
            return res
        return atMost(K) - atMost(K - 1)
