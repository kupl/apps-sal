from collections import defaultdict, deque


class Solution:

    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        graph = defaultdict(list)
        for (i, num) in enumerate(arr):
            graph[num].append(i)
        curr = [0]
        visited = set([0])
        jumps = 0
        while curr:
            nxt = []
            for node in curr:
                if node == n - 1:
                    return jumps
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nxt.append(child)
                graph[arr[node]].clear()
                for child in (node - 1, node + 1):
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nxt.append(child)
            curr = nxt
            jumps += 1
        return -1
