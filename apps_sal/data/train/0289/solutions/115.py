class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        l_sums = []
        m_sums = []
        flag_l = 0
        flag_m = 0
        
        l_sum_tmp = 0
        r_sum_tmp = 0
        for i in range(len(A)):
            if flag_l < L:
                flag_l += 1
                l_sum_tmp += A[i]
            else:
                l_sums.append(l_sum_tmp)
                l_sum_tmp += A[i] - A[i-L]
            
            if flag_m < M:
                flag_m += 1
                r_sum_tmp += A[i]
            else:
                m_sums.append(r_sum_tmp)
                r_sum_tmp += A[i] - A[i-M]
        m_sums.append(r_sum_tmp)
        l_sums.append(l_sum_tmp)
        
        max_sum = -1
        for i in range(len(m_sums)):
            for j in range(len(l_sums)):
                if i+M<=j or j+L<=i:
                    # print(m_sums[i], l_sums[j])
                    max_sum = max(m_sums[i]+l_sums[j], max_sum)
                    
        return max_sum
            
        
        return 1

