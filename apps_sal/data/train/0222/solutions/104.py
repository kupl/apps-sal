class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        s = set(A)
        n = len(A)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                (x, y) = (A[j], A[i] + A[j])
                length = 2
                while y in s:
                    (x, y) = (y, x + y)
                    length += 1
                count = max(count, length)
        return count if count >= 3 else 0
