class Solution:
    def minOperationsMaxProfit(self, lis: List[int], b: int, r: int) -> int:
        n = len(lis)
        q=pro=ans=tot=c=fin=0
        c=1
        for i in range(n):
            q+=lis[i]
            t = min(4,q)
            q-=t
            tot+=t
            pro = tot*b - r*(c)
            if pro>ans:
                ans=pro
                fin=c
       #     print(pro,ans,tot)
            c+=1
        while q>0:
            t = min(4,q)
            q-=t
            tot+=t
            pro = tot*b - r*(c)
            if pro>ans:
                ans=pro
                fin=c
        #    print(pro,ans,tot)
            c+=1
        if fin==0:
            fin=-1
        return fin
        
            

