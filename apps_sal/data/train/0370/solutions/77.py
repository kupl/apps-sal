mxn=10**5 +5
pri=[1]*(mxn)
for i in range(2,mxn):
    if pri[i]==1:
        pri[i]=i
        j=2
        while(i*j<mxn):
            if pri[i*j]==1:
                pri[i*j]=i
            j+=1

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        dct=[0]*mxn
        res=0
        def root(i):
            while(i!=arr[i]):
                i=arr[i]
                arr[i]=arr[arr[i]]
            return i
        def update(i,j):
            r1=root(i)
            r2=root(j)
            arr[r1]=r2
            size[r2]+=size[r1]
        for num in A:
            dct[pri[num]]+=1
        
        arr=[i for i in range(mxn)]
        size=[dct[i] for i in range(mxn)]
        
        for num in A:
            ls=[]
            while(num!=1):
                ls.append(pri[num])
                num=num//pri[num]
            if len(ls)==1:continue
            for i in range(1,len(ls)):
                if root(ls[0])!=root(ls[i]):
                    update(ls[0],ls[i])
    
                    
            
        return max(size)

