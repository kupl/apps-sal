
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        #minJump, shortest Path
        
        minJump = len(arr) + 1
        graph = {}
        for i, n in enumerate(arr):
            if 1 < i <len(arr)-1 and arr[i-1] == arr[i] == arr[i+1]:
                continue
            graph[n] = graph.get(n, [])
            graph[n].append(i)
        
        queue = collections.deque([0])
        visited = set([0])
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node == len(arr) - 1:
                    return step
                num = graph.pop(arr[node], [])
                for nei in [node + 1, node - 1] +num:
                    if nei not in visited and  0 <= nei < len(arr):
                        queue.append(nei)
                        visited.add(nei)
            step += 1

        
        
        

#         num2Index = {}
#         for i, item in enumerate(arr):
#             if i> 1 and i < len(arr)-1 and arr[i] == arr[i+1] == arr[i-1] : 
#                 continue
#             if item in num2Index:
#                 num2Index[item].append(i)
#             else:
#                 num2Index[item] = [i]
            

#         queue = [(0, 0)] 
#         visited = set({0})
#         step = 0

#         while queue:
#             size =len(queue)
#             for _ in range(size):
#                 pos, step = queue.pop(0)
#                 if pos == len(arr) -1 :
#                     return step
#                 num = num2Index.pop(arr[pos], [])
#                 for newpos in [pos + 1, pos - 1] + num:
#                     if 0 <= newpos < len(arr) and newpos != pos and newpos not in visited:
#                         visited.add(newpos)
#                         if newpos == len(arr) -1 :
#                             return step+1
#                         queue.append((newpos, step + 1))
                
#         return step

