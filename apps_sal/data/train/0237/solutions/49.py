class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        n = len(A)
        
        i, j, total, res = 0, 0, 0, 0
        while j < n:
            total += A[j]
            while i < j and total > S:
                total -= A[i]
                i += 1
            if total == S:
                res += 1
                # There could be multiple 0 between i & j.
                k = i
                while k < j and A[k] == 0:
                    k += 1
                    res += 1
            j += 1
        return res
