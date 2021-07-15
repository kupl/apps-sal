from collections import deque
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        adjList = {} 
        adjList[headID] = [] 
        for index, emp in enumerate(manager):
            if emp == -1:
                continue 
            if emp not in adjList: 
                adjList[emp] = []
            adjList[emp].append(index)
        
        queue = deque()        
        queue.append((headID, 0))

        maxMinutes = float('-inf')
        while queue:
            for i in range(len(queue)):
                idx, time = queue.popleft() 
                if informTime[idx] == 0:
                    maxMinutes = max(maxMinutes, time)
                else: 
                    for sub in adjList[idx]:
                        queue.append((sub, time+informTime[idx]))
                        
        return maxMinutes 
