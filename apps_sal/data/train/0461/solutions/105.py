import heapq


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        graph = collections.defaultdict(list)
        for i in range(len(manager)):
            u, v, w = manager[i], i, informTime[i]
            if v == -1:
                continue
            graph[u].append((v, w))

        queue = [(headID, informTime[headID])]
        seen = set()
        heapq.heapify(queue)
        time = {i: float('inf') for i in range(n)}
        time[headID] = 0

        while queue and len(seen) < n:
            f, dist = heapq.heappop(queue)
            seen.add(f)
            time[f] = min(time[f], dist)

            for nb, w in graph[f]:
                if nb not in seen:
                    heapq.heappush(queue, (nb, dist + w))

        maxi = max(time.values())

        return maxi if maxi < float('inf') else -1
