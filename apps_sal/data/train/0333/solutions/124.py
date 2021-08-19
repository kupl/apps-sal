from collections import deque, defaultdict


class Solution:

    def minJumps(self, arr: List[int]) -> int:
        idxs = defaultdict(set)
        for (idx, e) in enumerate(arr):
            idxs[e].add(idx)

        def bfs(idx):
            q = deque([0])
            step = -1
            not_visited = set(range(len(arr) - 1, 0, -1))
            while q:
                step += 1
                for _ in range(len(q)):
                    node = q.popleft()
                    if node == len(arr) - 1:
                        return step
                    nxt_nodes = idxs[arr[node]]
                    nxt_nodes = not_visited & nxt_nodes
                    for nxt in [node - 1, node + 1]:
                        if nxt in not_visited:
                            nxt_nodes.add(nxt)
                    if len(arr) - 1 in nxt_nodes:
                        return step + 1
                    not_visited.difference_update(nxt_nodes)
                    nxt_nodes = sorted(nxt_nodes, reverse=True)
                    q.extend(nxt_nodes)
            return -1
        bfs(0)
        return bfs(0)
