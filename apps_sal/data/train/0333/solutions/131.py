from collections import deque, defaultdict


class Solution:

    def minJumps(self, arr: List[int]) -> int:
        idxs = defaultdict(list)
        for (idx, e) in enumerate(arr):
            idxs[e].append(idx)

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
                    nxt_nodes = set(idxs[arr[node]] + [node + 1, node - 1])
                    nxt_nodes = not_visited & nxt_nodes
                    if len(arr) - 1 in nxt_nodes:
                        return step + 1
                    not_visited.difference_update(nxt_nodes)
                    nxt_nodes = sorted(nxt_nodes, reverse=True)
                    q.extend(nxt_nodes)
            return -1
        return bfs(0)
