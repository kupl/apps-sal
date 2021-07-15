class unionfind:
    def __init__(self,size):
        self.parent=[i for i in range(size+1)]
        self.rank=[0 for _ in range(size+1)]
    def find(self,x):
        if(x!=self.parent[x]):
            self.parent[x]=self.find(self.parent[x])
        return(self.parent[x])
    def union(self,x,y):
        px=self.find(x)
        py=self.find(y)
        if(px==py):
            return(px)
        if(self.rank[px]>self.rank[py]):
            self.parent[py]=px
            return(px)
        else:
            self.parent[px]=py
            if(self.rank[px]==self.rank[py]):
                self.rank[py]+=1
            return(py)

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
            
        dsu=unionfind(max(A))
        for i in A:
            for factor in range(2,int(sqrt(i))+1):
                if((i%factor)==0):
                    dsu.union(i,factor)
                    dsu.union(i,i//factor)
                    
        max_size = 0
        group_count = defaultdict(int)
        for a in A:
            group_id = dsu.find(a)
            group_count[group_id] += 1
            max_size = max(max_size, group_count[group_id])

        return max_size
