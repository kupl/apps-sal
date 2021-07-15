class Solution:
    def getKth(self, lo: int, hi: int, m: int) -> int:
        a=[i for i in range(lo,hi+1)]
        z=[]
        def cv(s,c,k):
            if s in k:
                k[s]=k[s]+1
            elif s%2==0:
                s=s/2
                c=c+1
            else:
                s=3*s+1
                c=c+1
            if s==1:
                return sum(k.values()),c
            return cv(s,c,k)
        for i in a:
            c=0
            k={}
            b=cv(i,c,k)
            z.append([b,i])
        z.sort(key=lambda x:x[0])
        a=[]
        for i in z:
            a.append(i[1])
        return a[m-1]  
        
           
            
        

