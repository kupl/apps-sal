class UnionFind:
    def __init__(self, N):
        self.par = list(range(N))
        self.rank = [0]*N
        self.size = [0]*N
    
    def find(self, x):
        if self.par[x]!=x:
            self.par[x]=self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        
        if px==py: return
        if self.rank[px]<self.rank[py]:
            self.par[px]=py
            self.size[py]+=self.size[px]
        elif self.rank[px]>self.rank[py]:
            self.par[py]=px
            self.size[px]+=self.size[py]
        else:
            self.par[py]=px
            self.size[px]+=self.size[py]
            self.rank[px]+=1

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        arr = [0]+arr
        N = len(arr)
        uf = UnionFind(N)
        res = []
        seen = set()
        matched = set()
        
        for i in range(1, N):
            seen.add(arr[i])
            matched.add(arr[i])
            uf.size[arr[i]]=1
            if arr[i]-1>=0 and arr[i]-1 in seen:
                uf.union(arr[i], arr[i]-1)
            if arr[i]+1<N and arr[i]+1 in seen:
                uf.union(arr[i], arr[i]+1)
                
            all_bigger = True
            for j in list(matched):
                idx = uf.find(j)
                if uf.size[idx]!=m:
                    matched.remove(j)

            if matched: 
                res.append(i)

        return res[-1] if res else -1
        
        
        
        

