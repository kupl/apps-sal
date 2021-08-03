class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        table = dict()

        for i in range(len(A)):
            for j in range(i + 1, len(A)):

                _diff = A[j] - A[i]
                if (i, _diff) in list(table.keys()):
                    table[j, _diff] = table[i, _diff] + 1
                else:
                    table[j, _diff] = 2

        return max(table.values())
