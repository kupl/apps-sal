import heapq


class Solution:

    def minDays(self, n: int) -> int:
        heap = [[0, n]]
        covered = set()
        while True:
            node = heapq.heappop(heap)
            if node[1] == 0:
                return node[0]
            if node[1] not in covered:
                covered.add(node[1])
                heapq.heappush(heap, [node[0] + 1, node[1] - 1])
            if node[1] % 2 == 0 and node[1] // 2 not in covered:
                covered.add(node[1])
                heapq.heappush(heap, [node[0] + 1, node[1] // 2])
            if node[1] % 3 == 0 and node[1] // 3 not in covered:
                covered.add(node[1])
                heapq.heappush(heap, [node[0] + 1, node[1] // 3])
