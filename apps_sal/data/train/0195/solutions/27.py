import numpy as np
class Solution:
    def countTriplets(self, A: List[int]) -> int:
        memo=dict()
        for i in range(len(A)):
            for j in range(i,len(A)):
                r=A[i]&A[j]
                memo[r]=memo.get(r,0)+(1 if i==j else 2) 
        ret=0
        for i in range(len(A)):
            for k in memo:
                if A[i]&k==0:
                    ret+=memo[k]
        return ret
