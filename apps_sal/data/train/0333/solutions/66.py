class Solution:

    def minJumps(self, arr: List[int]) -> int:
        minJump = len(arr) + 1
        graph = {}
        for (i, n) in enumerate(arr):
            if 1 < i < len(arr) - 1 and arr[i - 1] == arr[i] == arr[i + 1]:
                continue
            graph[n] = graph.get(n, [])
            graph[n].append(i)
        queue = collections.deque([0])
        visited = set([0])
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node == len(arr) - 1:
                    return step
                num = graph.pop(arr[node], [])
                for nei in [node + 1, node - 1] + num:
                    if nei not in visited and 0 <= nei < len(arr):
                        queue.append(nei)
                        visited.add(nei)
            step += 1
