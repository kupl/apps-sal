import math
class disjoint(object):
    def __init__(self, size):
        self.root_node_size = [1] * size
        self.nodes = [n for n in range(size)]
        
    def findRoot(self, node):
        while(self.nodes[node] != node):            
            node = self.nodes[node]
        return node
    
    def merge(self, val_one, val_two):
        root_one = self.findRoot(val_one)
        root_two = self.findRoot(val_two)
        
        if root_one == root_two:
            return
        
        r1size = self.root_node_size[root_one]
        r2size = self.root_node_size[root_two]
        
        new_root = None
        old_root = None
        if r1size <= r2size:
            new_root = root_two
            old_root = root_one
        else:
            new_root = root_one 
            old_root = root_two
        self.root_node_size[new_root] += self.root_node_size[old_root]
        self.root_node_size[old_root] = 0
        self.nodes[old_root] = new_root
        
class Solution:
    
    def largestComponentSize(self, A: List[int]) -> int:
        def factors(n):
            known_factors = set()
            while n % 2 == 0:
                known_factors.add(2)
                n //= 2
            for possible_factor in range(3, math.floor(math.sqrt(n))+1, 2):
                while n % possible_factor == 0:
                    known_factors.add(possible_factor)
                    n //= possible_factor
            if n > 2:
                known_factors.add(n)
            return known_factors
        
        dj = disjoint(len(A))
        known_factors = dict()
        for (i,v) in enumerate(A):
            for p in factors(v):
                if p in known_factors:
                    dj.merge(i, known_factors[p])
                known_factors[p] = i
        return max(dj.root_node_size)

