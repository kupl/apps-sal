import functools


class Solution:

    def tilingRectangle(self, n: int, m: int) -> int:
        """
        INF = n * m

        @functools.lru_cache(None)
        def dp(state):   # state是一个tuple, m个元素
            if n == min(state):
                return 0

            state = list(state)   # 从左到右铺
            mn = min(state)
            start = state.index(mn)
            res = INF
            for end in range(start,m):
                if state[end] != mn:
                    break
                side = end - start + 1
                if mn + side > n:
                    break
                state[start:end + 1] = [mn + side] * side
                res = min(res, dp(tuple(state)))
            return res + 1

        if m > n:   # 保证n大,保证高度最大宽度其次
            m, n = n, m
        return dp(tuple([0] * m))   # tuple做state
        """
        '\n        self.res = m * n\n        def dfs(height, moves):\n            if all(h == n for h in height):\n                self.res = min(self.res, moves)\n            if moves >= self.res:  # 剪枝\n                return \n            min_height = min(height)\n            idx = height.index(min_height)\n            ridx = idx + 1\n            while ridx < m and height[ridx] == min_height:  # 找到了一个最大的范围\n                ridx += 1\n            for i in range(min(ridx - idx, n - min_height), 0, -1):\n                new_height = height[:]\n                for j in range(i):\n                    new_height[idx + j] += i\n                dfs(new_height, moves + 1)\n        dfs([0] * m, 0)  # dfs的是目前的状态以及导致目前状态的操作步骤数\n        return self.res\n        '
        '\n        # A* algrithm\n        height = [0] * m\n        q = []\n        for i in range(min(m, n), 0, -1):\n            # push to heap: (guess, moves, -size, height)\n            heapq.heappush(q, (1, 1, -i, height)) # 这里的height是size还没用,待处理的\n        \n        while q:\n            guess, moves, neg_size, height = heapq.heappop(q)\n            size = -neg_size\n            \n            idx = height.index(min(height))  # 默认操作从左侧最低的位置装\n            height = height[:]    # 如果最小堆tuple弹出里有数组，用的时候，先把数组全部取一下[:]\n            for i in range(size):\n                height[idx + i] += size\n            if all(h == n for h in height):\n                return moves\n            \n            min_height = min(height)\n            idx = height.index(min_height)\n            ridx = idx + 1\n            while ridx < m and height[ridx] == min_height:\n                ridx += 1\n            for i in range(min(ridx - idx, n - min_height), 0, -1):\n                t = moves + 1 + len(set(h for h in height if h < n))\n                heapq.heappush(q, (t, moves + 1, -i, height))\n        '
        '\n        total_area = m * n\n        dp = [0] * (total_area + 1) # 使用dp的方法去(猜测)目前最少需要多少个square填满\n        for i in range(1, total_area + 1):\n            dp[i] = 1 + min(dp[i - k ** 2] for k in range(1, int(i ** 0.5) + 1))\n        \n        height = [0] * m\n        q = []\n        for i in range(min(m, n), 0, -1):\n            heapq.heappush(q, (1 + dp[total_area - i ** 2], 1, i, height))\n        \n        while q:\n            guess, moves, size, height = heapq.heappop(q)\n            \n            idx = height.index(min(height))\n            height = height[:]\n            for i in range(size):\n                height[idx + i] += size   #这里不能把i写成1\n            if all(h == n for h in height):\n                return moves\n            \n            min_height = min(height)\n            idx = height.index(min_height)\n            ridx = idx + 1\n            while ridx < m and height[ridx] == min_height:\n                ridx += 1\n            for i in range(min(ridx - idx, n - min_height), 0, -1):\n                guess = dp[total_area - sum(height) - i ** 2]\n                heapq.heappush(q, (guess + 1 + moves, moves + 1, i, height))\n        '

        @lru_cache(None)
        def dfs(i, j):
            if i == j:
                return 1
            if i == 1:
                return j
            if j == 1:
                return i
            res = i * j
            for x in range(1, i // 2 + 1):
                res = min(res, dfs(x, j) + dfs(i - x, j))
            for y in range(1, j // 2 + 1):
                res = min(res, dfs(i, y) + dfs(i, j - y))
            for leng in range(1, min(x, y)):
                for x in range(1, i - leng):
                    for y in range(1, j - leng):
                        res = min(res, dfs(x + leng, y) + dfs(i - (x + leng), y + leng) + dfs(x, j - y) + dfs(i - x, j - (y + leng)) + 1)
            return res
        return dfs(m, n)
