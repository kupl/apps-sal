class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # nested dict: k1 = difference, k2 = end idx of difference, val = count
        # max_len
        record = defaultdict(lambda: defaultdict(int))
        max_len = 0
        # go over list
        #   for num, get difference with all previous nums
        #       if difference in dict and second key is the same as previous num, add to dict[dif][self] = count+1, update max_len
        # return max_len
        for i, v_i in enumerate(A):
            for j in range(0, i):
                dif = v_i - A[j]
                if dif in record and j in record[dif]:
                    record[dif][i] = record[dif][j] + 1
                else:
                    record[dif][i] = 1
                max_len = max(max_len, record[dif][i])
        return max_len + 1
