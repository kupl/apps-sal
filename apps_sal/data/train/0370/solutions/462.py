class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def parent(x):
            while root[x]!=x:
                root[x]=root[root[x]]
                x=root[x]
            return x
        
        def union(x,y):
            px=parent(x)
            py=parent(y)
            if px!=py:
                if size[px]>size[py]:
                    px,py=py,px
                size[py]+=size[px]
                root[px]=py
                
        def factorize(index,val):
            while val!=1:
                if smallestPrimeFactor[val] not in factorParent:
                    factorParent[smallestPrimeFactor[val]]=index
                union(index,factorParent[smallestPrimeFactor[val]])
                val //= smallestPrimeFactor[val]
                
        m=max(A)+1
        smallestPrimeFactor=[i for i in range(m)]
        for i in range(2,int(pow(m,0.5))+1):
            if smallestPrimeFactor[i]==i:
                for j in range(i*i,m,i):
                    if smallestPrimeFactor[j]==j:
                        smallestPrimeFactor[j]=i
                        
        n=len(A)
        size=[1]*n
        root=[i for i in range(n)]
        factorParent={}
        for i in range(n):
            factorize(i,A[i])
        return max(size)
