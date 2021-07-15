class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        def traversal(A, L, M):
            maxi = 0
            for i in range(len(A)-L):
                L_slice = A[i:L+i]
                L_sum = sum(L_slice)
                
                for j in range(L+i,len(A)-M+1):
                    M_slice = A[j:M+j]
                    M_sum = sum(M_slice)
                    
                    maxi = max(maxi, L_sum+M_sum)
            return maxi
        forwards_sum = traversal(A,L,M)
        A.reverse()
        backwards_sum = traversal(A,L,M)
        return max(forwards_sum,backwards_sum)

