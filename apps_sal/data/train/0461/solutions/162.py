class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        if n == 1:
            return 0 

        graph = defaultdict(list)

        for idx, manager in enumerate(manager):
            graph[manager].append((informTime[manager], idx))
        

        pQueue = [(0, headID)]
        maxTime = 0 

        while pQueue:
            
            currTime , currId = heapq.heappop(pQueue)
            maxTime = max(maxTime, currTime)
            
            for nextTime, nei in graph[currId]:
                heapq.heappush(pQueue, (currTime + nextTime, nei))

        return maxTime
