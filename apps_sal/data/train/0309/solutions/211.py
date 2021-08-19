class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        N = len(A)
        table = []
        out = 0
        for i in range(N):
            table.append(defaultdict(dict))
            for j in range(0, i):
                js_table = table[j]
                diff = A[i] - A[j]
                if diff not in js_table:
                    table[i][diff] = 2
                else:
                    table[i][diff] = table[j][diff] + 1
                out = max(table[i][diff], out)
        return out
