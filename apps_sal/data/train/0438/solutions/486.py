# class UnionFind:
#     def __init__(self, n):
#         self.parent = {}
#         self.rank = [0] * (n+1)
#         self.group_size = defaultdict(list)
    
#     def find(self, x):
#         if x not in self.parent:
#             self.parent[x] = x
#             self.rank[x] = 1
#             self.group_size[1].append(x)

class UnionFind:
        def __init__(self, m, n):
            self.m = m
            self.parents = [i for i in range(n+1)]
            # self.ranks = [1 for _ in range(n)]
            self.group_size = defaultdict(set)
            # self.group_size[1] = set([i+1 for i in range(n)])
            self.sizes = defaultdict(int)
            # for i in range(n):
            #     self.sizes[i+1] = 1

        def find(self, x):
            if self.parents[x]!=x:
                self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

        def union(self, x, y):
            root_x, root_y = self.find(x), self.find(y)
            # print(\"x\", x ,\"y\", y)
            # print(\"root_x\", root_x ,\"root_y\", root_y)
            self.parents[root_x] = root_y
            size_root_x = self.sizes[root_x]
            self.sizes[root_x] = 0
            self.group_size[size_root_x].remove(root_x)

            size_root_y = self.sizes[root_y]
            self.group_size[size_root_y].remove(root_y)
            self.sizes[root_y] = size_root_y + size_root_x
            self.group_size[self.sizes[root_y]].add(root_y)
            
            
            # print(\"len(self.group_size[self.m])\", len(self.group_size[self.m]))
            if len(self.group_size[self.m])>0:
                return True
            else:
                return False
            

class Solution:
    ## my own solution: union find
    ## mapping between sizes and positions
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        uf = UnionFind(m, n)
        # print(uf.group_size)
        # print(uf.sizes)
        seen = set()
        res = -1
        for idx, x in enumerate(arr):
            seen.add(x)
            uf.sizes[x] = 1
            uf.group_size[1].add(x)
            if x-1 in seen:
                uf.union(x, x-1)
                # if len(uf.group_size[m])>0:
                #     res = idx+1
            if x+1 in seen:        
                uf.union(x+1, x)
                
            if len(uf.group_size[m])>0:
                res = idx+1
            # print(\"uf.group_size\", uf.group_size)
            # print(\"uf.sizes\", uf.sizes)
        return res
            

