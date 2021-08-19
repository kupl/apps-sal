class Solution:

    def canReach(self, arr: List[int], start: int) -> bool:
        graph = {}
        for i in range(len(arr)):
            graph[i] = []
            if arr[i] == 0:
                continue
            if i + arr[i] < len(arr):
                graph[i] += [i + arr[i]]
            if i - arr[i] >= 0:
                graph[i] += [i - arr[i]]
        stack = [start]
        seen = set([start])
        while len(stack) > 0:
            curr = stack.pop()
            seen.add(curr)
            if len(graph[curr]) == 0 and arr[curr] == 0:
                return True
            for adj in graph[curr]:
                if adj not in seen:
                    stack.append(adj)
        return False
