class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        par=[-1]*100001
        def find1(x):
            if par[x]==-1:
                return x
            par[x]=find1(par[x])
            return par[x]
        
        def union1(x,y):
            xp=find1(x)
            yp=find1(y)
            if xp!=yp:
                par[yp]=xp
        
        for x in A:
            for i in range(2,int(sqrt(x))+1):
                if x%i==0:
                    union1(i,x)
                    union1(x,x//i)
                    
        cnt=0
        cach={}
        for x in A:
            xp=find1(x)
            cnt=max(cnt,1+cach.get(xp,0))
            cach[xp]=1+cach.get(xp,0)
        return cnt

