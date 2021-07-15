class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        dp = [[0, 0, 0] for _ in range(len(A))]
        L, M = min(L, M), max(L, M)
        l_sum, m_sum = 0, 0
        for idx in range(L + M):
            if idx <= L - 1:
                l_sum += A[idx]
                if idx == L - 1:
                    dp[idx][0] = l_sum
            else:
                l_sum += A[idx] - A[idx - L]
                dp[idx][0] = l_sum if dp[idx - 1][0] < l_sum else dp[idx - 1][0]
            if idx <= M - 1:
                m_sum += A[idx]
                if idx == M - 1:
                    dp[idx][1] = m_sum
            else:
                m_sum += A[idx] - A[idx - M]
                dp[idx][1] = m_sum if dp[idx - 1][1] < m_sum else dp[idx - 1][1]              
        dp[L + M - 1][2] = max(l_sum + dp[idx - L][1], m_sum + dp[idx - M][0])
        for idx in range(L + M, len(A)):
            l_sum += A[idx] - A[idx - L]
            dp[idx][0] = l_sum if dp[idx - 1][0] < l_sum else dp[idx - 1][0]
            m_sum += A[idx] - A[idx - M]
            dp[idx][1] = m_sum if dp[idx - 1][1] < m_sum else dp[idx - 1][1]
            print((idx, l_sum, m_sum, dp[idx - L], dp[idx - M]))
            dp[idx][2] = max(dp[idx - 1][2], l_sum + dp[idx - L][1], m_sum + dp[idx - M][0])
        print(dp)
        return dp[len(A) - 1][2]

