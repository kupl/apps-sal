class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        # dp = {prev_val, next_val: len}
        n = len(A)
        dp = [[2] * n for _ in range(n)]
        loc = {A[0]: 0, A[1]: 1}
        longest = 0
        for k in range(2, n):
            loc[A[k]] = k
            for j in range(k):
                target = A[k] - A[j]
                if target in loc and loc[target] < j:
                    dp[j][k] = dp[loc[target]][j] + 1
                    longest = max(longest, dp[j][k])

        return longest

        '''dp = {}
        dp[(A[1], A[0] + A[1])] = 2
        for i in range(2, len(A)):
            for j in range(i):
                if (A[j], A[i]) not in dp:
                    dp[(A[i], A[j] + A[i])] = 2
                else:
                    dp[(A[i], A[j] + A[i])] = dp[(A[j], A[i])] + 1
                    del dp[(A[j], A[i])]
        longest = max(dp.values())
        
        return longest if longest > 2 else 0'''
