class Solution:

    def dfs(self, graph, arr, root):
        stack = []
        stack.append(root)
        visited = set()
        while len(stack) > 0:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            if arr[current] == 0:
                return True
            for n in graph.get(current, []):
                stack.append(n)
        return False

    def canReach(self, arr: List[int], start: int) -> bool:
        graph = dict()
        for i in range(len(arr)):
            graph[i] = graph.get(i, [])
            if 0 <= i + arr[i] < len(arr):
                graph[i].append(i + arr[i])
            if 0 <= i - arr[i] < len(arr):
                graph[i].append(i - arr[i])
        return self.dfs(graph, arr, start)


if False:
    print(Solution().canReach([4, 2, 3, 0, 3, 1, 2], 0))
    print(Solution().canReach([3, 0, 2, 1, 2], 2))
