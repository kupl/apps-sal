class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        S = set(A)
        n = len(A)
        res = 0
        for i in range(n):
            for j in range(i+1,n):
                x, y = A[j],A[i] + A[j]
                ans = 2
                while y in S:
                    x, y = y, x + y
                    ans += 1
                res = max(res, ans)
        return res if res >= 3 else 0
    
    
    

