class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        res = 1
        cnt = 1
        
        for i in range(1, len(A)):
            if A[i]==A[i-1]:
                cnt = 1
            elif i>1 and (A[i-2]-A[i-1])*(A[i-1]-A[i])<0:
                cnt += 1
            else:
                cnt = 2
            
            res = max(res, cnt)
            
        return res

