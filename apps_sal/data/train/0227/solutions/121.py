class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        i, j = 0, 0
        res = 0
        zeroes = K
        count = [0]
        while i < len(A):
            if A[i] == 0:
                zeroes -= 1
            if zeroes < 0:
                if A[j] == 0:
                    zeroes += 1
                j += 1
            i += 1
            res = max(res, i - j)
        return res
