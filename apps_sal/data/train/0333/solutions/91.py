class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        arr_f = []
        prev = None
        repeat = 0
        for num in arr:
            if num == prev:
                if repeat == 2:
                    continue
                repeat += 1
            else:
                prev = num
                repeat = 0
            arr_f.append(num)
        n = len(arr_f)

        graph = {}
        for i in range(n):
            if arr_f[i] in graph:
                graph[arr_f[i]].append(i)
            else:
                graph[arr_f[i]] = [i]

        curs = [0]
        visited = {0}
        step = 0

        while curs:
            nex = []

            for node in curs:
                if node == n - 1:
                    return step

                for child in graph[arr_f[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                graph[arr_f[node]].clear()

                for child in [node - 1, node + 1]:
                    if 0 <= child < n and child not in visited:
                        visited.add(child)
                        nex.append(child)

            curs = nex
            step += 1

        return -1
