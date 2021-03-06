class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        res = 0
        i = 0
        for j in range(len(A)):
            if A[j] == 0:
                K -= 1
            res = max(res, j - i)
            while K < 0:
                if A[i] == 0:
                    K += 1
                i += 1
        return max(res, len(A) - i)
