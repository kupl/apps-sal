class Solution:
    def largestSumOfAverages(self, A: List[int], k: int) -> float:
        n=len(A)
        mtr=[[0 for i in range(n+1)] for j in range(k+1)]
        # mtr[k][n]
        for i in range(n):
            mtr[1][i]=sum(A[:i+1])/(i+1)
        for i in range(2,k+1):
            for j in range(n):
                for x in range(j+1):
                    # print(\"(\",mtr[i-1][x],\",\",x,\")\",mtr[i-1][x]+(sum(A[x:j])/(j-x)),i,x,j)
                    mtr[i][j] = max(mtr[i][j],mtr[i-1][x-1]+(sum(A[x:j+1])/(j+1-x)))
        # for i in mtr:
        #     print(i)
        
        ans=sys.maxsize *(-1)
        for i in range(1,k+1):
            ans=max(ans,mtr[i][-2])
        return ans

