class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        res = 0
        zeros = 0
        n = len(A)
        i = 0
        for j in range(n):
            zeros += A[j] == 0
            if zeros <= K:
                res = max(res, j - i + 1)
            if zeros > K:
                zeros -= A[i] == 0
                i += 1
        return res
