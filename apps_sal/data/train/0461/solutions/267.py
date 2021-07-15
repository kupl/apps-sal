class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        G = {i:[] for i in range(n)} # map node to a list of its children
        for i in range(len(manager)):
            if manager[i] > -1:
                G[manager[i]].append(i)
        self.ans = 0
        def dfs(root=headID,timeUsed=0):
            if not G[root]:
                #self.ans = max(self.ans,timeUsed)
                return timeUsed
            # for child in G[root]:
            #     dfs(child,timeUsed + informTime[root])
            
            return max([dfs(child,timeUsed + informTime[root]) for child in G[root]])
        
        return dfs()
        
        
#         from collections import deque
#         def bfs(root=headID):
#             ans = 0
#             Q = deque()
#             Q.append([root])
            
#             while Q:
#                 nodes = Q.popleft()
#                 ans += max([informTime[node] for node in nodes])
                
#                 next_lvl = []
#                 for node in nodes:
#                     for child in G[node]:
#                         next_lvl.append(child)
#                 if next_lvl:
#                     Q.append(next_lvl)
#             return ans
#         return bfs()

