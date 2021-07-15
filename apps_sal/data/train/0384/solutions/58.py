class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        if not A: return 0
        n=len(A)
        A.sort()
        ans = 0
        for i in range(n):
            ans += A[i]*(1<<i)
            ans -= A[i]*(1<<(n-i-1))
            ans %= (10**9+7)
        return ans
            

