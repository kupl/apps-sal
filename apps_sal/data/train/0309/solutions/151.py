class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        diffs = [collections.defaultdict(int) for _ in range(len(A))]
        diffs[0][0] = 1
        max_len = 1
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in diffs[j]:
                    diffs[i][diff] = diffs[j][diff] + 1
                else:
                    diffs[i][diff] = 2

                max_len = max(max_len, diffs[i][diff])

        return max_len
