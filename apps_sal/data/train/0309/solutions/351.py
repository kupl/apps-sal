class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        table = dict()
        longest_subseq = float('-inf')
        for row in range(len(A)):
            for col in range(0, row):
                change = A[row] - A[col]
                if (col, change) in table:
                    table[row, change] = 1 + table[col, change]
                else:
                    table[row, change] = 2
                longest_subseq = max(longest_subseq, table[row, change])
        return longest_subseq
