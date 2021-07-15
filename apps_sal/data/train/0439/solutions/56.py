class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        size = len(A)
        if(size <= 1):
            return size
        inc = 1
        dec = 1
        best = 1
        for i in range(1,size):
            if(A[i-1] > A[i]):
                dec = inc + 1
                inc = 1
            elif(A[i-1] < A[i]):
                inc = dec + 1
                dec = 1
            else:
                inc = dec = 1
            best = max(best,inc, dec)
        return best
                

