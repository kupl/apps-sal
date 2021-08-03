class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        def atMostK(kk):
            counter = collections.Counter()
            res = ii = 0
            for jj in range(len(A)):
                if counter[A[jj]] == 0:
                    kk -= 1
                counter[A[jj]] += 1
                while kk < 0:
                    counter[A[ii]] -= 1
                    if counter[A[ii]] == 0:
                        kk += 1
                    ii += 1
                res += jj - ii + 1
            return res
        return atMostK(K) - atMostK(K - 1)
