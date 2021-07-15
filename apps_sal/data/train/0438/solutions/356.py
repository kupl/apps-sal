class Group:
    def __init__(self, x, y):
        self.left = x
        self.right = y
        # self.update()
        self.n = y - x + 1
        
#     def update(self):
#         self.n = self.right - self.left + 1
        
#     def add_left(self, x):
#         self.left = x
#         self.update()
        
#     def add_right(self, y):
#         self.right = y
#         self.update()
    
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        groups = [None] * (1+len(arr))
        group_size = collections.defaultdict(int)
        visited = set()
        res = -1
        for step, x in enumerate(arr, 1):
            visited.add(x)
            left = right = x
            lsize = rsize = 0
            if x>1 and x-1 in visited:
                left = groups[x-1].left
                lsize = groups[x-1].n
            if x<len(arr) and x+1 in visited:
                right = groups[x+1].right
                rsize = groups[x+1].n
            g = Group(left, right)
            groups[left] = g
            groups[right] = g
            group_size[lsize+rsize+1] += 1
            if lsize != 0:
                group_size[lsize] -= 1
            if rsize != 0:
                group_size[rsize] -= 1
                
            if group_size[m] > 0:
                res = step
        return res
                
        
#         def find(parent, i):
#             if parent[i] == -1:
#                 return i 
#             if parent[i] != -1:
#                 return find(parent, parent[i]) 

#         def union(parent, x, y): 
#             px = find(parent, x) 
#             py = find(parent, y) 
#             parent[px] = py
            
#         parent = [-1] * (1+len(arr))
#         for x in arr:
#             parent[x] = x
#             if x > 1 and parent[x-1] != -1:
#                 union(parent, x, y)
#                 parent[x] = x
            
        

