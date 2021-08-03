from collections import deque
from functools import reduce


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if not arr:
            return False
        if arr[start] == 0:
            return True

        def add_edge(nodes, edge):
            index, jump = edge
            if jump == 0:
                nodes[index].append(index)
                return nodes
            if (back := index - jump) >= 0:
                nodes[index].append(back)
            if (forw := index + jump) < len(arr):
                nodes[index].append(forw)
            return nodes

        edges = reduce(add_edge, enumerate(arr), defaultdict(list))

        q = deque([start])
        visited = {start}
        while q:
            popped = q.popleft()
            for n in edges[popped]:
                if n == popped:
                    return True
                if n in visited:
                    continue
                visited.add(n)
                q.append(n)
        return False
