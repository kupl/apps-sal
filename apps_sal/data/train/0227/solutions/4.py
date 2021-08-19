class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        (i, j, count, res) = (0, 0, 0, 0)
        while j < len(A):
            if A[j] == 0:
                count += 1
            while count > K:
                if A[i] == 0:
                    count -= 1
                i += 1
            res = max(res, j - i + 1)
            j += 1
        return res
