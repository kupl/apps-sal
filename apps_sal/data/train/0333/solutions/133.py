from collections import defaultdict, deque


class Solution:

    def minJumps(self, arr: List[int]) -> int:
        node_h = defaultdict(list)
        graph = defaultdict(set)
        for (idx, val) in enumerate(arr):
            node_h[val].append(idx)
        q = deque()
        visited = set()
        q.append((0, 0))
        visited.add(0)
        while q:
            (node, level) = q.popleft()
            if node == len(arr) - 1:
                return level
            nbrs = node_h[arr[node]]
            nbrs.append(node - 1)
            nbrs.append(node + 1)
            for nbr in nbrs:
                if nbr == len(arr) - 1:
                    return level + 1
                if nbr >= 0 and nbr < len(arr) and (nbr not in visited):
                    q.append((nbr, level + 1))
                    visited.add(nbr)
            node_h[arr[node]] = []
        return 0
