class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        dp={}
        position={}
        # for i in range(len(cuts)):
        #     position[cuts[i ]]=i
        cuts.sort()
        def f(s,e):
            if (s,e) in dp:
                return dp[(s,e)]
            else:
                res=float('inf')
                i=0
                while i<len(cuts) and cuts[i]<=s:
                    i+=1
                # print(\"i\"+str(i))
                j=len(cuts)-1
                while cuts[j]>=e and j>=0:
                    j-=1
                # print(j)
                if i>j:
                    dp[(s,e)]=0
                    return 0
                for k in range(i,j+1):
                    # dp[(s,e)]=dp[(s,cuts[k])]+dp[(cuts[k],e )]  +s-e
                    res=min(res,f(s,cuts[k])+f(cuts[k],e)+e-s)
                dp[(s,e)]=res
                return dp[(s,e)]

        return f(0,n)
