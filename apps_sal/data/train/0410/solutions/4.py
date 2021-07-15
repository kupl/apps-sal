class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        d={}
        for i in range(lo,hi+1):
            c=0
            t=i
            while(i!=1):
                if i%2==0:
                    i=i//2
                    c+=1
                    
                else:
                    i=3*i+1
                    c+=1
            d[t]=c
        f=sorted(list(d.items()),key=lambda kv: kv[1])
        return f[k-1][0]

