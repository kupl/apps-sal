class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        cumsum = []
        N = len(A)
        for i in range(N):
            if i == 0:
                cumsum.append(A[i])
            else:
                cumsum.append(cumsum[i - 1] + A[i])
        l_sums = []
        i = 0
        while i + L <= N:
            l_sums.append(cumsum[i + L - 1] - cumsum[i] + A[i])
            i += 1
        m_sums = []
        i = 0
        while i + M <= N:
            m_sums.append(cumsum[i + M - 1] - cumsum[i] + A[i])
            i += 1
        i = 0
        j = len(m_sums) - 1
        ans = 0
        for i in range(len(l_sums)):
            for j in range(i + L, len(m_sums)):
                curr_sum = l_sums[i] + m_sums[j]
                ans = max(ans, curr_sum)
        for i in range(len(m_sums)):
            for j in range(i + M, len(l_sums)):
                curr_sum = m_sums[i] + l_sums[j]
                ans = max(ans, curr_sum)
        return ans
