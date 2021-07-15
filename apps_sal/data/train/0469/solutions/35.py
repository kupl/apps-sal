from typing import List
from collections import defaultdict

class DS:
    
    def __init__(self, n):
        self.sz = [1] * n
        self.rt = [i for i in range(n)]
        self.ccCt = n
        
    def query(self, x):
        root = x
        while root != self.rt[root]:
            self.rt[root] = self.rt[self.rt[root]]
            root = self.rt[root]
        return root
    
    def union(self, x, y):
        rootX, rootY = self.query(x), self.query(y)
        if rootX != rootY:
            self.ccCt -= 1
            szX, szY = self.sz[rootX], self.sz[rootY]
            if szX < szY:
                self.sz[rootY] += szX
                self.rt[rootX] = rootY
            else:
                self.sz[rootX] += szY
                self.rt[rootY] = rootX
                
    def cc(self):
        return self.ccCt

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        ds = DS(n)
        edgeCt = 0
        for node in range(n):
            l, r = leftChild[node], rightChild[node] 
            for c in (l, r):
                if c != -1:
                    edgeCt += 1
                    ds.union(node, c)
        return (n - 1 == edgeCt) and ds.cc() == 1
    
    

