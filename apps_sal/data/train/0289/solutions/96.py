class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        sums = list(itertools.accumulate(A))
        def get_sums(n):
            return [(sums[i]-sums[i-n] if i-n >= 0 else sums[i], i-n+1, i) for i in range(n-1, len(sums))]
            
        l_sums = get_sums(L)
        m_sums = get_sums(M)
        max_sum = float('-inf')
        for l_sum, l_i, l_j in l_sums:
            for m_sum, m_i, m_j in m_sums:
                if m_j < l_i or l_j < m_i:
                    max_sum = max(max_sum, m_sum + l_sum)
        
        return max_sum
        
        
        # we know there will be len - (L+M) elements excluded
        # there will a stretch between before them
        # iterate through looking for the larger array sum
        # search in the left and right remainders for the smaller array sum of size x

