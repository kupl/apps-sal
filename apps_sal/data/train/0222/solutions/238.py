class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        S = set(A)
        maxLen = 0
        n = len(A)
        for i in range(0, n):
            for j in range(i + 1, n):

                x = A[j]
                y = A[i] + A[j]
                length = 2

                while y in S:

                    z = x + y
                    x = y
                    y = z
                    length += 1
                    maxLen = max(maxLen, length)

        return maxLen if maxLen >= 3 else 0
