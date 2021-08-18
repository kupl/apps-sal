class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:

        index_mapping = {number: index for index, number in enumerate(A)}
        memory = [[2 for i in range(len(A))] for j in range(len(A))]

        max_len = 0
        for k in range(len(A)):
            for j in range(k):
                i_num = A[k] - A[j]
                if i_num in index_mapping and index_mapping[i_num] < j:
                    i = index_mapping[i_num]
                    memory[j][k] = memory[i][j] + 1
                    max_len = max(max_len, memory[j][k])
        return max_len if max_len >= 3 else 0
