class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        max_len = 2
        alen = len(A)
        len_index = [{} for index in range(alen)]
        len_index[1] = {A[1] - A[0]: 2}
        for idx in range(2, alen):
            val = A[idx]
            indices = len_index[idx]
            for preidx in range(idx):
                diff = val - A[preidx]
                if diff in len_index[preidx]:
                    new_len = len_index[preidx][diff] + 1
                else:
                    new_len = 2
                if diff in indices:
                    indices[diff] = max(indices[diff], new_len)
                else:
                    indices[diff] = new_len
                max_len = max(max_len, new_len)
        return max_len
