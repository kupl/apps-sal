class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        N = len(A)
        if N == 0: return 0
        mod = 10**9 + 7                
        
        res = 0
        s = []
        A = [0] + A + [0]
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res % mod

