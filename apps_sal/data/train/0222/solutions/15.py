class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        
#         # Time Complexity: O(N^2)
#         # Space Complesity:  O(NlogM)
        
#         index_mapping = {num:index for index, num in enumerate(A)}
#         memory = collections.defaultdict(lambda: 2)
#         # memory[j, k] = memory[i, j] + 1
#         # memory[i, j] a fibonacci subsequence ending with A[i] A[j]
        
#         # index i, j, k
#         result = 0
#         for k, k_num in enumerate(A):
#             for j in range(k):
#                 i = index_mapping.get(k_num - A[j])
#                 if i is not None and i < j:
#                     # (i, j) can connect to (j, k)
#                     memory[j, k] = memory[i, j] + 1
#                     result = max(memory[j, k] , result)  
        
#         return result if result >=3 else 0  # n >= 3


        # 还是老老实实用array matrix来做memorization好了
        # Time Complexity: O(N^2)
        # Space Complesity:  O(N^2)
        index_mapping = {number:index for index, number in enumerate(A)}
        memory = [[2 for i in range(len(A))] for j in range(len(A))]
        
        max_len = 0
        for k in range(len(A)):
            for j in range(k):
                i_num = A[k] - A[j]
                if i_num in index_mapping and index_mapping[i_num] < j:
                    i = index_mapping[i_num]
                    memory[j][k] = memory[i][j] + 1
                    max_len = max(max_len, memory[j][k] )
        return max_len if max_len >= 3 else 0
                    
        
        
        

