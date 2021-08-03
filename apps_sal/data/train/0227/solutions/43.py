class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:

        lo, hi = 0, 0
        zmax = 0
        n_k = 0
        while hi < len(A):
            # print(f\"{lo},{hi}, {zmax}\")
            if A[hi] == 0:
                n_k += 1
            # break

            while n_k > K:
                if A[lo] == 0:
                    n_k -= 1
                lo += 1

            zmax = max(zmax, hi - lo + 1)

            hi += 1
        return zmax
