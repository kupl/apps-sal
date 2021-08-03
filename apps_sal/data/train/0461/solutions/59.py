# class Solution:
#     def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
# #BFS
#         stack = [(headID, 0)]

#         ans = 0
#         dic = {}
#         for e, m in enumerate(manager):
#             dic[m] = dic.get(m, set())
#             dic[m].add(e)

#         while stack:
#             em, time = stack.pop()
#             if informTime[em] == 0:
#                 ans = max(ans, time)
#             else:
#                 for e in dic.get(em, []):
#                     stack.append((e, informTime[em]+ time))
#         return ans

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
                heapq.heappush(heap, (time + w, v))
        return max(dist.values())
