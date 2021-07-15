class Solution(object):
    def maxTurbulenceSize(self, A):
        def cmp(a, b):
            if a == b:
                return 0
            elif a > b:
                return 1
            else:
                return -1
        a = 0
        ans = 1
        N = len(A)
        for i in range(1, N):
            c = cmp(A[i-1], A[i])
            if c == 0:
                a = i
            elif i == N-1 or c*cmp(A[i],A[i+1]) != -1:
                ans = max(ans, i-a+1)
                a = i
        return ans
