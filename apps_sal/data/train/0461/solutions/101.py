class Tree:
    def __init__(self):
        pass

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = {}
        
        for i,val in enumerate(manager):
            if val in graph:
                graph[val].append(i)
            else:
                graph[val] = [i]
        
        ans = BFS(headID,informTime,graph)
        return ans

def BFS(root,informTime,graph):
        queue = [(root,0)]
        maxTime = 0
        
        while(len(queue)):
            currElem = queue.pop(0)
            node = currElem[0]
            currTime = currElem[1]
            
            CurrInformTime = informTime[node]
            
            timeToNext = currTime+CurrInformTime
            maxTime = max(timeToNext,maxTime)
                    
            if node in graph:
                children = graph[node]
                for i in children:
                    queue.append((i,timeToNext))
        
        return maxTime
