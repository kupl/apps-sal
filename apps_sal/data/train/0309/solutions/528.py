class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        pos = defaultdict(int)
        best = 1
        for i in range(len(A) - 1, -1, -1):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                if (j, diff) in pos:
                    pos[i, diff] = max(pos[i, diff], pos[j, diff] + 1)
                else:
                    pos[i, diff] = max(pos[i, diff], 2)
                best = max(best, pos[i, diff])
        return best
