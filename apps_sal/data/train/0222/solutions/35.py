class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        s = set(A)
        n = len(A)
        
        
        def getlength(a, b):
            l = 0
            
            temp = a + b
            if temp in s:
                l = 2
            else: return 0
            
            while temp in s:
                temp, b = temp + b, temp
                l += 1
            
            return l
        
        mx = 0
        for i in range(n):
            for j in range(i+1, n):
                ll = getlength(A[i], A[j])
                if mx < ll:
                    mx = ll
        
        return mx
