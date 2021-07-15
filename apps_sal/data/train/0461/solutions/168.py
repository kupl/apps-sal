import heapq

class Solution:
    def numOfMinutes(self, N: int, H: int, M: List[int], T: List[int]) -> int:
        graph = defaultdict(lambda:[])
        for i, m in enumerate(M):
            if i != H:
                graph[m].append(i)

        cnt = 0; heap = []
        heapq.heappush(heap, (T[H], H))
        while heap:
            cur = heapq.heappop(heap)
            cnt += 1
            if cnt == N:
                return cur[0]
            if cur[1] in graph:
                for sub in graph[cur[1]]:
                    heapq.heappush(heap, (T[sub]+cur[0], sub))


