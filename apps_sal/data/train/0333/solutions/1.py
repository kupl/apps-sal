from collections import deque


class Solution:

    def minJumps(self, arr: list) -> int:
        if len(arr) == 1:
            return 0
        graph = {}
        for (i, n) in enumerate(arr):
            if n in graph:
                graph[n].append(i)
            else:
                graph[n] = [i]
        curs = [0]
        other = [len(arr) - 1]
        visited = {0}
        visited2 = {len(arr) - 1}
        step = 0
        while curs:
            is_curs = len(curs) <= len(other)
            if not is_curs:
                (curs, other) = (other, curs)
                (visited, visited2) = (visited2, visited)
            nex = []
            for node in curs:
                for child in graph[arr[node]]:
                    if child in visited2:
                        return step + 1
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)
                for child in [node - 1, node + 1]:
                    if child in visited2:
                        return step + 1
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)
            curs = nex
            step += 1
        return -1
