class Solution:

    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        graph = collections.defaultdict(set)
        for i in range(n):
            if i + arr[i] < n:
                graph[i].add(i + arr[i])
            if i - arr[i] >= 0:
                graph[i].add(i - arr[i])
        end = set([i for i in range(n) if arr[i] == 0])
        q = [start]
        visited = set([start])
        while q:
            x = q.pop(0)
            for i in graph[x]:
                if i in end:
                    return True
                if i not in visited:
                    visited.add(i)
                    q.append(i)
        return False
