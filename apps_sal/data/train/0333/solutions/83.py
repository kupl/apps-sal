from collections import defaultdict


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        '''
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = [0]  
        visited = {0}
        step = 0

        while curs:
            nex = []

            for node in curs:
                if node == n-1:
                    return step

                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                graph[arr[node]].clear()

                for child in [node-1, node+1]:
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)

            curs = nex
            step += 1

        return -1
        '''
        m = defaultdict(list)
        for i in range(len(arr)):
            m[arr[i]].append(i)
        start = (0, 0)
        queue = [start]
        visited = set([0])
        while queue != []:
            current = queue.pop(0)
            if current[0] == len(arr) - 1:
                return current[1]
            if current[0] + 1 < len(arr) and current[0] + 1 not in visited:
                queue.append((current[0] + 1, current[1] + 1))
                visited.add(current[0] + 1)
            if current[0] - 1 >= 0 and current[0] - 1 not in visited:
                queue.append((current[0] - 1, current[1] + 1))
                visited.add(current[0] - 1)
            for n in m[arr[current[0]]]:
                if n not in visited:
                    queue.append((n, current[1] + 1))
                    visited.add(n)
            if arr[n] in m:
                del m[arr[n]]
