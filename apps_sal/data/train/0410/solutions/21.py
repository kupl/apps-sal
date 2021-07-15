class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def fun(n):
            if n==1:return 0
            ans=0
            while n>1:
                if n%2==0:
                    n//=2
                else:
                    n=n*3+1
                ans+=1
            ans+=1
            return ans
        ans=[] 
        for i in range(lo,hi+1):
            ans.append([i,fun(i)])
        ans.sort(key=lambda x:x[1])
        for i in range(k):
            if i==k-1:
                return ans[i][0]
        

