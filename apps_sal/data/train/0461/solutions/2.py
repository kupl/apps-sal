# class Node:
#     def __init__(self, id: int, inform_t: int):
#         self.id = id
#         self.children = []
#         self.inform_t = inform_t
    
#     def __repr__(self):
#         return f'<{self.id} ({self.inform_t}): {len(self.children)}>'
    
#     def total_inform_time(self):
#         t = self.inform_t
#         if self.children:
#             t += max(ch.total_inform_time() for ch in self.children)
#         return t

# class Solution:
    
#     def build_tree(self, manager: List[int], inform_time: List[int]) -> Node:
#         nodes = [None] * len(manager)
#         root = None
#         for id, man_id in enumerate(manager):
#             if nodes[id] is None:
#                 nodes[id] = Node(id, inform_time[id])
            
#             if man_id >= 0:
#                 if nodes[man_id] is None:
#                     nodes[man_id] = Node(man_id, inform_time[man_id])

#                 nodes[man_id].children.append(nodes[id])
#             else:
#                 root = nodes[id]
#         return root
    
    
#     def numOfMinutes(self, n: int, head_id: int, manager: List[int], inform_time: List[int]) -> int:
#         root = self.build_tree(manager, inform_time)
#         return root.total_inform_time()
    

# Top down
# class Solution:
#     def numOfMinutes(self, n: int, head_id: int, manager: List[int], inform_time: List[int]) -> int:
#         children = [[] for _ in range(n)]
#         for id, man_id in enumerate(manager):
#             if man_id >= 0:
#                 children[man_id].append(id)
        
#         def dfs(id):
#             t = inform_time[id]
#             if children[id]:
#                 t += max(dfs(ch) for ch in children[id])
#             return t
        
#         return dfs(head_id)
 
    
# Bottom up
# class Solution:
#     def numOfMinutes(self, n: int, head_id: int, manager: List[int], inform_time: List[int]) -> int:
        
#         def dfs(id):
#             if manager[id] >= 0:
#                 inform_time[id] += dfs(manager[id])
#                 manager[id] = -1
#             return inform_time[id]
        
#         return max(dfs(id) for id in range(n))


# Bottom up with cache
class Solution:
    def numOfMinutes(self, n: int, head_id: int, manager: List[int], inform_time: List[int]) -> int:
        cache = [None] * n
        
        def dfs(id):
            if cache[id]:
                return cache[id]
            
            t = inform_time[id]
            if manager[id] >= 0:
                t += dfs(manager[id])
            
            cache[id] = t
            return t
        
        return max(dfs(id) for id in range(n))

