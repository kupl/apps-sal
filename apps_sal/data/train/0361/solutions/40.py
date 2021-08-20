class Solution:

    def tilingRectangle(self, n: int, m: int) -> int:
        if n == m:
            return 1
        if n > m:
            (n, m) = (m, n)
        layers0 = [0 for _ in range(n)]
        visited = {}
        ans = [n * m]

        def dfs(layers, stepsNow):
            if stepsNow > ans[0]:
                return
            key = tuple(layers)
            if key in visited and stepsNow >= visited[key]:
                return
            visited[key] = stepsNow
            minH = m + 1
            i0 = -1
            for (i, h) in enumerate(layers):
                if h < minH:
                    minH = h
                    i0 = i
            if minH == m:
                ans[0] = min(ans[0], stepsNow)
                return
            minHWidth = 0
            maxL = m - minH
            for i in range(i0, n):
                if layers[i] == minH:
                    minHWidth += 1
                else:
                    break
            maxL = min(maxL, minHWidth)
            for l in range(maxL, 0, -1):
                nextLayers = list(key)
                for i in range(i0, i0 + l):
                    nextLayers[i] += l
                dfs(nextLayers, stepsNow + 1)
            return
        dfs(layers0, 0)
        return ans[0]
