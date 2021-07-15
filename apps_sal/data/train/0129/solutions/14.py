class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        a, b, n = 0, 1, len(A)
        def opt(i,j):
            return A[i] + A[j] + i - j
        
        ans = [A[0], opt(0,1)] + [0 for _ in range(n-2)]
        
        for i in range(2, n):
            opt_a, opt_b = opt(a, i), opt(b, i)
            if opt_a > opt_b:
                ans[i] = opt_a
                b = i
            else:
                ans[i] = opt_b
                a = b
                b = i
        
        return max(ans)

