class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        # to i, there are 2^(i)  subsequence with max A[i]
        # there are 2^(n-i-1) subseq with min A[i]

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
            # print(i,k,ans)

            ans += ((1 << (i))) * k

            ans -= ((1 << (n - i - 1))) * k
            #ans += k*(pow(2,i)- pow(2, n-i-1))
        return ans % (10**9 + 7)
