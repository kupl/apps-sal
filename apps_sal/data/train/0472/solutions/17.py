class Solution:
    # returns an adjacency list representation of graph
    def genGraph(self, arr: List[int]) -> List[List[int]]:
        adjList = [[] for i in range(len(arr))]
        for i in range(len(arr)):
            left = i - arr[i]
            right = i + arr[i]
            if left >= 0:
                adjList[i].append(left)
            if right < len(arr):
                adjList[i].append(right)
        return adjList
    
    def canReach(self, arr: List[int], start: int) -> bool:
        graph = self.genGraph(arr)
        bfsQueue = [start]
        visited = set()
        while len(bfsQueue) > 0:
            node = bfsQueue.pop(0)
            if arr[node] == 0:
                return True
            if node in visited:
                break
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    bfsQueue.append(neighbour)
        return False
