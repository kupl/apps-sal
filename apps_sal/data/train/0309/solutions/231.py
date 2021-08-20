class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        cache = dict()
        maxi = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                if (diff, i) in cache:
                    cache[diff, j] = 1 + cache[diff, i]
                else:
                    cache[diff, j] = 2
                if maxi < cache[diff, j]:
                    maxi = cache[diff, j]
        return maxi
