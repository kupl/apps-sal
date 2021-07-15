class UnionFind:
     def __init__(self, n:int)->None:
        self.parent = [i for i in range(n)]
        
     def find(self, x:int)->int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
     def union(self, a:int, b:int):
        self.parent[self.find(b)] = self.find(a)

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        uf = UnionFind(100001)
        for x in A:
            for i in range(2,int(sqrt(x))+1):
                if x % i == 0:
                    uf.union(i,x)
                    uf.union(x,x//i)
        count = 0
        hashMap = {}
        for x in A:
            xp = uf.find(x)
            count = max(count,1 + hashMap.get(xp,0))
            hashMap[xp] = 1 + hashMap.get(xp,0)
        return count
        
        
                
        
                
            

