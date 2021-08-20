class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        inputs = {i: 0 for i in range(n)}
        graph = {i: set() for i in range(n)}
        for (i, m) in enumerate(manager):
            if m == -1:
                continue
            if i not in graph[m]:
                graph[m].add(i)
                inputs[i] += 1
        stack = [(headID, 0)]
        ans = 0
        while stack:
            (i, elapsed) = stack.pop()
            ans = max(ans, elapsed)
            new_elapsed = elapsed + informTime[i]
            for nb in graph[i]:
                inputs[nb] -= 1
                if inputs[nb] == 0:
                    stack.append((nb, new_elapsed))
        return ans
