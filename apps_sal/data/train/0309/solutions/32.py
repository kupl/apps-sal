class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        cache = [{} for i in range(len(A))]
        m = 0

        n = len(A)
        for i in range(1, n):
            for j in range(i):
                diff = A[i] - A[j]
                if diff not in cache[j]:
                    cache[i][diff] = 2
                else:
                    cache[i][diff] = cache[j][diff] + 1
                if cache[i][diff] > m:
                    m = cache[i][diff]

        return m
