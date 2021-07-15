
import math

class UnionFind:
    
    def __init__(self , size):
        self.id = [i for i in range(size)]
        
    def find(self , p):
        
        root = p
        while root != self.id[root]:
            root = self.id[root]
        
        while p != root:
            nxt = self.id[p]
            self.id[p] = root
            p = nxt
            
        return root
    
    
    def unify(self , p , q):
        
        root1 = self.find(p)
        root2 = self.find(q)
        if root1 == root2 : return 
        
        self.id[root2] = root1
            
        

        
    
    
        
        
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        
        max_val = max(A)
        uf = UnionFind(max_val + 1) # +1 for ease of access
        for num in A:
            for i in range(2 , int(math.sqrt(num))+1):
                if num % i == 0:
                    uf.unify(num , i)
                    uf.unify(num , num//i)
        
        parent_count = {}
        cur_max = 1
        for num in A:
            parent = uf.find(num)
            parent_count[parent] = 1 + parent_count.get(parent , 0)
            cur_max = max(cur_max , parent_count[parent])
            
        return cur_max
    
            
    

