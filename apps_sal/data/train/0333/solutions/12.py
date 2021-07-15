#Bidirectional BFS
class Solution:
    def minJumps(self, arr: List[int]) -> int:        
        if len(arr) < 2:
            return 0
        
        graph = {} #存每個值的index
        for i in range(len(arr)):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]
                
        cur = [0] #目前這步要拜訪的index
        visited = {0}
        step = 0
        
        other = [len(arr) - 1] #另一個沒走過的部分
        
        while cur:
            #從較小的開始搜尋
            if len(cur) > len(other):
                cur, other = other, cur
            
            nex = [] #下一步要拜訪的index
            
            for i in cur:
                # check same value
                for node in graph[arr[i]]:
                    if node in other:
                        return step + 1
                    if node not in visited:
                        visited.add(node)
                        nex.append(node)
                graph[arr[i]].clear()  #避免重複拜訪
                
                for x in [i + 1, i - 1]:
                    if x in other:
                        return step + 1
                    if 0 <= x < len(arr) and x not in visited:
                        visited.add(x)
                        nex.append(x)
            cur = nex
            step += 1

