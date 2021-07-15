class DSU():
    
    def __init__(self,n):
        self.parent=list(range(n))
        self.size=[1]*n
    
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        xp,yp=self.find(x),self.find(y)
        
        if xp==yp:
            return False
        
        if self.size[xp]<self.size[yp]:
            xp,yp=yp,xp
        
        self.size[xp]+=self.size[yp]
        self.parent[yp]=xp
        
        return True

class Solution:
    
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        dsu=DSU(n)
        
        for i in range(n):
            
            if leftChild[i]>=0 and not dsu.union(i,leftChild[i]):
                return False
            if rightChild[i]>=0 and not dsu.union(i,rightChild[i]):
                return False
        
        p=dsu.find(0)
        for i in range(n):
            if p != dsu.find(i):
                return False
        
        return True
