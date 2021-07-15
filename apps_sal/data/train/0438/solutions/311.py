

import collections
class Node:
    def __init__(self, val):
        self.size = 1
        self.val = val
        self.parent = self
        
class UnionFind:
    def __init__(self):
        self.map = {}
        self.sizes = collections.defaultdict(int)
        
    def find(self, node):
        if node.val not in self.map:
            self.map[node.val] = node
            self.sizes[node.size] += 1
        elif node.parent != node:
            node = self.find(node.parent)
        return node
    
    
    def merge(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 != parent2:
            if parent1.size >= parent2.size:
                self.sizes[parent1.size] -= 1
                self.sizes[parent2.size] -= 1
                parent2.parent = parent1
                parent1.size += parent2.size
                self.sizes[parent1.size] += 1
            else:
                self.sizes[parent1.size] -= 1
                self.sizes[parent2.size] -= 1
                parent1.parent = parent2
                parent2.size += parent1.size
                self.sizes[parent2.size] += 1

class Solution:
    def findLatestStep(self, arr, m: int) -> int:
        uf = UnionFind()
        ans = -1
        for i, val in enumerate(arr):
            node = Node(val)
            uf.find(node)
            if val - 1 in uf.map:
                uf.merge(node, uf.map[val - 1])
            if val + 1 in uf.map:
                uf.merge(node, uf.map[val + 1])
                
            if uf.sizes[m] > 0:
                ans = i + 1
        return ans
