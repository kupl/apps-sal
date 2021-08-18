class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        record = defaultdict(lambda: defaultdict(int))
        max_len = 0
        for i, v_i in enumerate(A):
            for j in range(0, i):
                dif = v_i - A[j]
                if dif in record and j in record[dif]:
                    record[dif][i] = record[dif][j] + 1
                else:
                    record[dif][i] = 1
                max_len = max(max_len, record[dif][i])
        return max_len + 1
