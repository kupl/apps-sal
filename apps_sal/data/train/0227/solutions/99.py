class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        (i, j, n) = (0, 0, len(A))
        for x in A:
            j += 1
            if x == 0:
                K -= 1
            if K < 0:
                if A[i] == 0:
                    K += 1
                i += 1
        return j - i
