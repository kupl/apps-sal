class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        (i, res) = (0, 0)
        for j in range(len(A)):
            K -= 1 - A[j]
            while K < 0:
                K += 1 - A[i]
                i += 1
            res = max(res, j - i + 1)
        return res
