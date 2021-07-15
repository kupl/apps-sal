class dsu:
    def __init__(self,n):
        self.parent=list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]    
    
    def union(self, x, y):
        
        px, py = self.find(x), self.find(y)
        
        if px==py:
            return False
        if px != py:
            self.parent[px] = py
            return True

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        DSU=dsu(n)
        indegree=[0]*n
        for i in range(n):
            if(leftChild[i]!=-1):
                indegree[leftChild[i]]+=1
            if(rightChild[i]!=-1):
                indegree[rightChild[i]]+=1
      
        count_zeroes=0
        for i in indegree:
            if(i==0):
                count_zeroes+=1
            if(count_zeroes>1):
                return False
        for node,child in enumerate(zip(leftChild,rightChild)):
            if child[0]!=-1:
                if(DSU.union(node,child[0])==False):
                    return False
            if child[1]!=-1:
                if(DSU.union(node,child[1])==False):
                    return False    
                
        return True
        
        

