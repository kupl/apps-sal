mod_ = 10**9 + 7

class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        n = len(A)
        p_2 = [1]
        for i in range(1,n+2):
            p_2.append((p_2[-1]*2)%mod_)
        l = [0]
        for i in range(1,n):
            l.append( (2*l[-1] + (A[i]-A[i-1]) * (p_2[i]-1) ) % mod_ )
        sol = 0
        for elem in l:
            sol = (sol + elem) % mod_
        return sol
