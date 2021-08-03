from collections import deque


class Solution:
    def minJumps(self, arr: List[int]) -> int:

        # construct graph
        n = len(arr)
        graph = collections.defaultdict(list)
        for i, num in enumerate(arr):
            graph[num].append(i)

        # bfs
        queue = deque([0])
        visited = set([0])

        steps = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                curr_idx = queue.popleft()
                if curr_idx == n - 1:
                    return steps
                for nxt_idx in [curr_idx - 1, curr_idx + 1] + graph[arr[curr_idx]][::-1]:
                    if 0 <= nxt_idx < n and nxt_idx not in visited:
                        if nxt_idx == n - 1:
                            return steps + 1
                        queue.append(nxt_idx)
                        visited.add(nxt_idx)
            steps += 1

        return -1
