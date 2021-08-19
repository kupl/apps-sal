"""
subseq: non contiguous

B[i+1] - B[i] is always the same 
for each we need the last elt in seq 

goal: return the length of longest 

state:
i, last in seq, diff, length of the seq 

helper(i, last, diff, l)

choices:
 - use (condition A[i] - last == diff)
 - skip 
 - start looking for a new arith seq ? 

use: 
if A[i] - last == diff:
    helper(i + 1, A[i], diff, l + 1)
    
helper(i+1, last, diff, l)

if i > 0:
    helper(i + 1, A[i], A[i] - A[i - 1], 2)
   
dp[(i, diff)]: length of longest arith seq ending at i with difference diff 


"""
from functools import lru_cache


class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = {}
        for i in range(n):
            for j in range(i + 1, n):
                d = A[j] - A[i]
                dp[j, d] = dp.get((i, d), 1) + 1
        return max(dp.values())
