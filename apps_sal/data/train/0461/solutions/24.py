class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        
        for i in range(len(manager)):
            graph[manager[i]].append((informTime[i], i))
        heap = [(informTime[headID], headID)]
        # dic = {}
        mx = -1
        while heap:
            time, index = heapq.heappop(heap)
            mx = max(mx,time)

            for t,n in graph[index]:
                heapq.heappush(heap, (t+time, n))
        return mx#max(dic.values())

