from collections import defaultdict, deque

class Solution:
    
    def canReach(self, arr: List[int], start: int) -> bool:
        zero_value = set([])
        
        for i in range(len(arr)):
            if arr[i] == 0:
                zero_value.add(i)
        
        # bfs
        queue = deque([start])
        seen = set([])
        while queue:
            i = queue.popleft()
            if i in zero_value:
                return True
            seen.add(i)

            up = i + arr[i]
            if up < len(arr) and up not in seen:
                queue.append(up)
            down = i - arr[i]
            if down >=0 and down not in seen:
                queue.append(down)
        
        return False

#     def canReach(self, arr: List[int], start: int) -> bool:
#         graph = defaultdict(set)
#         zero_value = set([])
        
#         for i in range(len(arr)):
#             if arr[i] == 0:
#                 zero_value.add(i)
#             else:
#                 if i + arr[i] < len(arr):
#                     graph[i].add(i + arr[i])
#                 if i - arr[i] >=0:
#                     graph[i].add(i - arr[i]) 
        
#         # bfs
#         queue = deque([start])
#         seen = set([])
#         while queue:
#             item = queue.popleft()
#             if item in zero_value:
#                 return True
#             seen.add(item)

#             for nei in graph[item]:
#                 if nei not in seen:
#                     queue.append(nei)
        
#         return False

