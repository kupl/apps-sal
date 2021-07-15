class Solution:
    def minJumps(self, arr: List[int]) -> int:
        indexes = collections.defaultdict(list)
        for idx, v in enumerate(arr):
            indexes[v].append(idx)
        #early pruning.
        for key in indexes:
            indexes[key] = [
                v
                for j, v in enumerate(indexes[key]) 
                if not (
                    1 <= j < len(indexes[key]) - 1 
                    and indexes[key][j-1]==v-1 
                    and indexes[key][j+1]==v+1
                )
            ]
        
        queue, visited = collections.deque([(0, 0)]), set([0])
        
        while queue:
            idx, jumps = queue.popleft()
            if idx == len(arr) - 1:
                return jumps
            
            v = arr[idx]
            for j in [idx + 1, idx - 1] + indexes[v][::-1]:
                if 0 <= j < len(arr) and j not in visited:
                    visited.add(j)
                    queue.append((j, jumps + 1))
                    
# class Solution:
#     def minJumps(self, arr: List[int]) -> int:
#         a_i = collections.defaultdict(list)
#         for i, a in enumerate(arr):
#             a_i[a].append(i)
#         def bfs():
#             from collections import deque
#             Q = deque([(0,0)])
#             seen = {0}
#             while Q:
#                 i, d = Q.popleft()
#                 if i==len(arr)-1:return d
#                 for j in [i-1, i+1]+a_i[arr[i]][::-1]:
#                     if 0<=j<len(arr) and j!=i and j not in seen:
#                         seen.add(j)
#                         if j==len(arr)-1:return d+1
#                         Q.append((j,d+1))
#         return bfs()

