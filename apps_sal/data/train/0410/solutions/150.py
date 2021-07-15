class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        d=dict()
        for i in range(lo,hi+1):
            a=i
            c=0
            while(a>1):
                if(a%2==0):
                    a=a/2
                    c+=1
                else:
                    a=3*a+1
                    c+=1
            d[i]=c
        res=sorted(list(d.items()), key=lambda x:x[::-1])
        return(res[k-1][0])

