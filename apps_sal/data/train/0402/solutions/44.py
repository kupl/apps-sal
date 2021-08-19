import heapq


def solve(b, s, t):

    def create_priority_item(c, t):
        dx = c[0] - t[0]
        dy = c[1] - t[1]
        d2 = dx * dx + dy * dy
        return (d2, c)
    b = set((tuple(_b) for _b in b))
    s = tuple(s)
    t = tuple(t)
    heap = [(-1, s)]
    visited = set()
    iter = -1
    while heap:
        iter += 1
        if iter > 110000.0:
            return False
        (_, c) = heapq.heappop(heap)
        if c in visited:
            continue
        if c[0] < 0 or c[0] >= 1000000.0 or c[1] < 0 or (c[1] >= 1000000.0):
            continue
        if c in b:
            continue
        if c == t:
            return True
        visited.add(c)
        x = c[0]
        while t[0] > x and (x + 1, c[1]) not in b:
            x += 1
        heapq.heappush(heap, create_priority_item((x, c[1]), t))
        x = c[0]
        while t[0] < x and (x - 1, c[1]) not in b:
            x -= 1
        heapq.heappush(heap, create_priority_item((x, c[1]), t))
        y = c[1]
        while t[1] > y and (c[0], y) not in b:
            y += 1
        heapq.heappush(heap, create_priority_item((c[0], y), t))
        y = c[1]
        while t[1] < y and (c[0], y) not in b:
            y -= 1
        heapq.heappush(heap, create_priority_item((c[0], y), t))
        heapq.heappush(heap, create_priority_item((c[0] + 1, c[1]), t))
        heapq.heappush(heap, create_priority_item((c[0] - 1, c[1]), t))
        heapq.heappush(heap, create_priority_item((c[0], c[1] + 1), t))
        heapq.heappush(heap, create_priority_item((c[0], c[1] - 1), t))
    return False


class Solution:

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        return solve(blocked, source, target)
