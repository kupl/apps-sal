class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)
        
        for i, managerId in enumerate(manager):
            graph[managerId].append((informTime[i], i))
        
        dist = {}
        heap = [(informTime[headID], headID)] 
        
        while heap:
            time, u = heapq.heappop(heap)
            if u in dist:
                continue
            dist[u] = time    
            for w, v in graph[u]:
                if v in dist:
                    continue
                heapq.heappush(heap, (time+w, v))    
        return max(dist.values()) 
