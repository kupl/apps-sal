class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        '''
        dp = {}
        for i in xrange(len(A)):
            for j in xrange(i + 1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        return max(dp.values())
        '''
        l=len(A)
        dp={}
        c=collections.defaultdict(list)
        for i in range(l-1):
            for j in range(i+1,l):
                #c[(i,j)]=A[i]-A[j]
                c[i].append(A[i]-A[j])
                dp[j,A[j]-A[i]]=dp.get((i,A[j]-A[i]),1)+1
        #print(c)
        return max(dp.values())
        res=2
        #for i in range(l-1):
            #analyze c[i]
            

