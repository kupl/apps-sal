class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        if not A: return 0
        ans = 0
        A.sort()
        for i, n in enumerate(A):
            ans += ((1<<i)-(1<<(len(A)-i-1)))*n
            
        return ans%(10**9+7)

