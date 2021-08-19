class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        table = []
        for (i, z) in enumerate(A):
            table.append(collections.defaultdict(lambda: 1))
            for j in range(i):
                diff = z - A[j]
                table[i][diff] = table[j][diff] + 1
        return max((max(y.values()) for y in table))
