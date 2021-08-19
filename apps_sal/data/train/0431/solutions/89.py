class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:

        # # Naive DP N^2 time, N space, over time limit
        # n = len(A)
        # md = 10**9+7
        # pre = A.copy()
        # res = sum(pre)
        # for i in range(1,n):
        #     now = [0]*(n-i)
        #     for j in range(n-i):
        #         now[j] = min(pre[j],pre[j+1])
        #         res = (res+now[j]) % md
        #     pre = now
        # return res

        # Copied from discussion
        res = 0
        s = []
        A = [0] + A + [0]
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res % (10**9 + 7)
