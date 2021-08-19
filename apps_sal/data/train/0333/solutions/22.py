class Solution:

    def minJumps1(self, arr: List[int]) -> int:
        if not arr:
            return 0
        dp = [float('inf')] * len(arr)
        dp[0] = 0
        minIdx = {arr[0]: (0, 0)}
        for i in range(1, len(arr)):
            x = arr[i]
            stepRight = dp[i - 1] + 1
            jumpStep = minIdx[x][1] + 1 if x in minIdx else float('inf')
            dp[i] = min(stepRight, jumpStep)
            if x in minIdx:
                if dp[i] < minIdx[x][1]:
                    minIdx[x] = (i, dp[i])
            else:
                minIdx[x] = (i, dp[i])
            j = i - 1
            while j >= 0 and dp[j] > dp[j + 1] + 1:
                dp[j] = dp[j + 1] + 1
                y = arr[j]
                if dp[j] < minIdx[y][1]:
                    minIdx[y] = (j, dp[j])
                j -= 1
        return dp[-1]

    def minJumps(self, arr: List[int]) -> int:
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
                if node == n - 1:
                    return step
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)
                graph[arr[node]].clear()
                for child in [node - 1, node + 1]:
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)
            curs = nex
            step += 1
        return -1
