class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # table[index][diff] equals to the length of
        # arithmetic sequence at index with difference diff.
        table = dict()
        max_v = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):

                _diff = A[j] - A[i]
                if (i, _diff) in table.keys():
                    table[j, _diff] = table[i, _diff] + 1
                else:
                    table[j, _diff] = 2  # the first diff
                    # will corrspond to two values [v1,v2]
                max_v = max(max_v, table[j, _diff])

        return max_v
