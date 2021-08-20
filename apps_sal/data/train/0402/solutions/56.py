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
    heap = [s]
    visited = set()
    iter = -1
    while heap:
        iter += 1
        if iter > 110000.0:
            return False
        c = heap.pop()
        if c in visited or c in b or c[0] < 0 or (c[0] >= 1000000.0) or (c[1] < 0) or (c[1] >= 1000000.0):
            continue
        if c == t:
            return True
        dx = c[0] - s[0]
        dy = c[1] - s[1]
        if dx * dx + dy * dy > 200 * 200:
            return True
        visited.add(c)
        heap.append((c[0] + 1, c[1]))
        heap.append((c[0] - 1, c[1]))
        heap.append((c[0], c[1] + 1))
        heap.append((c[0], c[1] - 1))
    return False


def solve_both(b, s, t):
    return solve(b, s, t) and solve(b, t, s)


class Solution:

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        return solve_both(blocked, source, target)
