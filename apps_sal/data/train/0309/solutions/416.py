class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return n

        counts = [{} for _ in A]
        max_count = 0

        for i in range(0, len(A)):
            for j in range(0, i):
                diff = A[i] - A[j]
                counts[i][diff] = max(counts[i].get(diff, 1), counts[j].get(diff, 1) + 1)
                max_count = max(max_count, counts[i][diff])

        return max_count

