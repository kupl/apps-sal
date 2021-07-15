class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) <= 2:
            if len(A) == 2 and A[0] == A[1]:
                return 1
            return len(A)
        res = 0
        start = 0
        end = 0
        for i in range(1, len(A)-1):
            if A[i-1] < A[i] > A[i+1] or A[i-1] > A[i] < A[i+1]:
                end = i + 1
                res = max(res, end - start + 1)
            else:
                start = i
        if res == 0:
            if max(A) != min(A):
                return 2
            else:
                return 1
        return res

                
                
                
                

