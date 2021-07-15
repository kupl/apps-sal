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

        curs = [0]  # store current layers
        visited = {0}
        step = 0

        # when current layer exists
        while curs:
            nex = []

            # iterate the layer
            for node in curs:
                # check if reached end
                if node == n-1:
                    return step

                # check same value
                for child in graph[arr_f[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                # clear the list to prevent redundant search
                graph[arr_f[node]].clear()

                # check neighbors
                for child in [node-1, node+1]:
                    if 0 <= child < n and child not in visited:
                        visited.add(child)
                        nex.append(child)

            curs = nex
            step += 1

        return -1
