class Solution:

    def canReach(self, arr: List[int], start: int) -> bool:
        from collections import defaultdict
        graph = defaultdict(list)
        length = len(arr)
        for i in range(len(arr)):
            if arr[i] != 0:
                if i - arr[i] >= 0:
                    graph[i].append(i - arr[i])
                if i + arr[i] < length:
                    graph[i].append(i + arr[i])
        zeroindex = [i for (i, j) in enumerate(arr) if j == 0]
        visited = []
        print(graph, zeroindex)

        def dfs(s, visited):
            if s in zeroindex:
                return True
            if s in visited:
                return False
            visited.append(s)
            for i in graph[s]:
                if dfs(i, visited):
                    return True
            return False
        return dfs(start, visited)
