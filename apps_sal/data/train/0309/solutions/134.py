class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        memo = {}
        
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                diff = A[j] - A[i]
                memo[j, diff] = memo.get((i, diff), 1) + 1
                
        return max(memo.values())
