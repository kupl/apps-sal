class Solution:
    def less_than(self,A,i,j):
        for r in range(len(A)):
            if ord(A[r][i]) > ord(A[r][j]):
                return False
        return True
    
    def minDeletionSize(self, A: List[str]) -> int:
        #for r in A:
        #    print(r)
        # for i in range(1,len(A[0])):
        #     print(self.less_than(A,i-1,i))
        n = len(A[0])
        dp = [ 1 for i in range(n)]
        
        for i in range(1,n):
            #print(\"i=\",i)
            j = i-1
            while(j>=0):
                #print(j,i,self.less_than(A,j,i))
                if self.less_than(A,j,i):
                    dp[i] = max(dp[i],dp[j]+1)
                j -=1
            #print(i,dp)
        
        return n-max(dp)
                       
        

