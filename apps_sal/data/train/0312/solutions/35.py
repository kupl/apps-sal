class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        S = [0]
        res = float('inf')
        for num in A:
            S.append(S[-1] + num)
        q = []
        for i, s in enumerate(S):
            while q and S[q[-1]] >= s:
                q.pop()
            while q and S[q[0]] + K <= s:
                cur_i = q.pop(0)
                res = min(res, i - cur_i)
            q.append(i)
        if res == float('inf'):
            return -1
        else:
            return res
        # n = len(A)
        # dp = [[0]*n for _ in range(n)]
        # res = float('inf')
        # for i in range(len(A)):
        #     if i == 0:
        #         dp[0][i] = A[i]
        #     else:
        #         dp[0][i] = dp[0][i-1] + A[i]
        #     if dp[0][i] >= K:
        #         res = min(res, i+1)
        # for i in range(1,n):
        #     for j in range(i,n):
        #         dp[i][j] = dp[i-1][j] - A[i-1]
        #         if dp[i][j] >= K:
        #             res = min(res, j-i+1)
        # if res == float('inf'):
        #     return -1
        # return res
