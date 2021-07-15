class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        
        sequences = [defaultdict(int) for _ in range(len(A))]
        
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                sequences[i][diff] = max(sequences[j][diff]+1, sequences[i][diff])
        
        return max(max(mapping.values()) for mapping in sequences[1:]) + 1
                

