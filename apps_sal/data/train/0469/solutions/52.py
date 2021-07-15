class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x != parent_y:
            self.parent[parent_x] = parent_y
            self.count -= 1
            
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [0] * n
        
        uf = UnionFind(n)
        
        for prev, childs in enumerate(zip(leftChild, rightChild)):
            l, r = childs
            if l != -1:
                parent[l] += 1
                uf.union(l, prev)
            if r != -1:
                parent[r] += 1
                uf.union(r, prev)
        
        return sum(parent) == n-1 and uf.count == 1

