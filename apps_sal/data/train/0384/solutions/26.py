class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()

        ans = 0
        '''
        for i in range(len(A)):
            for j in range(i,len(A)):
                if i == j:continue
                if A[i] == A[j]: continue
                ans +=(1<< ( j-i-1))*(A[j]-A[i])
        '''
        n = len(A)
        for i, k in enumerate(A):

            ans += ((1 << (i))) * k

            ans -= ((1 << (n - i - 1))) * k
        return ans % (10**9 + 7)
