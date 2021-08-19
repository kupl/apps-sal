from collections import defaultdict, deque


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        node_h = defaultdict(list)
        graph = defaultdict(set)

        # Constructring graph based on these rules
        # i + 1 where: i + 1 < arr.length.
        # i - 1 where: i - 1 >= 0.
        # j where: arr[i] == arr[j] and i != j.
        for idx, val in enumerate(arr):
            # if idx - 1 >= 0:
            #     graph[idx].add(idx-1)
            # if idx + 1 < len(arr):
            #     graph[idx].add(idx+1)
            # for node_idx in node_h[val]:
            #     # graph[idx].add(node_idx)
            #     graph[val].add(idx)
            #     # graph[node_idx].add(idx)
            node_h[val].append(idx)

        q = deque()
        visited = set()
        q.append((0, 0))
        visited.add(0)

        while (q):
            node, level = q.popleft()
            if node == len(arr) - 1:
                return level
            nbrs = node_h[arr[node]]
            nbrs.append(node - 1)
            nbrs.append(node + 1)
            # for nbr in graph[node]:
            for nbr in nbrs:
                if nbr == len(arr) - 1:
                    return level + 1
                if nbr >= 0 and nbr < len(arr) and nbr not in visited:
                    q.append((nbr, level + 1))
                    visited.add(nbr)
            node_h[arr[node]] = []  # [BUG] Clearing this is crucial otherwise we might revisit the node again, causing TLE

        return 0

# [NOTE] First attempt failed with large input of same numbers with just the last number different :)
# https://leetcode.com/submissions/detail/397710738/testcase/

# Clearing up the processed node list helped with TLE better explanation here
# https://leetcode.com/problems/jump-game-iv/discuss/502699/JavaC++-BFS-Solution-Clean-code-O(N)/445620
