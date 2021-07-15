class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        '''
            [0,6,5,2,2,5,1,9,4]
            
            [0,6,11,13,15,20,21,30,34]
                       i i
            
            max_sum = -?
        
        '''
        
        summ = 0
        
        for i in range(len(A)):
            summ += A[i]
            A[i] = summ
        
        
        max_sum = -float('inf')
        for i in range(len(A) - L + 1):
            if i - 1 > -1:
                L_sum = A[i+L - 1] - A[i - 1]
            else:
                L_sum = A[i+L - 1]
            M_max_sum = -float('inf')
            for j in range(i - M + 1):
                if j - 1 > -1:
                    M_sum = A[j+M-1] - A[j - 1]
                else:
                    M_sum = A[j+M-1]
                M_max_sum = max(M_max_sum, M_sum)
            
            for j in range(i+L, len(A) - M + 1):
                if j - 1 > -1:
                    M_sum = A[j+M-1] - A[j - 1]
                else:
                    M_sum = A[j+M-1]
                M_max_sum = max(M_max_sum, M_sum)
            
            max_sum = max(max_sum, L_sum + M_max_sum)
        
        
        return max_sum
