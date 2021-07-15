from collections import defaultdict
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:    
        count = 0
        memo = defaultdict(int)
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                num1 = A[i]
                num2 = A[j]
                diff = A[j] - num1
                val = memo[(num1,diff,i)] + 1
                memo[(num2, diff,j)] = val
                count = max(val, count)
        return count + 1 if count > 0 else count

                    
                    

