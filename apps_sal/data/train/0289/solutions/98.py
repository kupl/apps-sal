class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        self.cum = [A[0]]
        
        for i in range(1, len(A)):
            self.cum.append(self.cum[i-1] + A[i])
            
        largest = 0
        for i in range(len(A) - L + 1):
            l_sum = self.cum[i+L-1] - self.cum[i] + A[i]
            m_sum = 0
            for j in range(i - M + 1):
                m_sum = max(m_sum, self.cum[j+M-1] - self.cum[j] + A[j])

            for j in range(i+L, len(A) - M +1):
                m_sum = max(m_sum, self.cum[j+M-1] - self.cum[j] + A[j])

            largest = max(largest, l_sum + m_sum)
                
        
        return largest

