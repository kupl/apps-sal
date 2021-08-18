import functools


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        '''
        INF = n * m

        @functools.lru_cache(None)
        def dp(state):   
            if n == min(state):
                return 0

            state = list(state)   
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

        if m > n:   
            m, n = n, m
        return dp(tuple([0] * m))   
        '''
        '''
        self.res = m * n
        def dfs(height, moves):
            if all(h == n for h in height):
                self.res = min(self.res, moves)
            if moves >= self.res:  
                return 
            min_height = min(height)
            idx = height.index(min_height)
            ridx = idx + 1
            while ridx < m and height[ridx] == min_height:  
                ridx += 1
            for i in range(min(ridx - idx, n - min_height), 0, -1):
                new_height = height[:]
                for j in range(i):
                    new_height[idx + j] += i
                dfs(new_height, moves + 1)
        dfs([0] * m, 0)  
        return self.res
        '''
        '''
        height = [0] * m
        q = []
        for i in range(min(m, n), 0, -1):
            heapq.heappush(q, (1, 1, -i, height)) 
        
        while q:
            guess, moves, neg_size, height = heapq.heappop(q)
            size = -neg_size
            
            idx = height.index(min(height))  
            height = height[:]    
            for i in range(size):
                height[idx + i] += size
            if all(h == n for h in height):
                return moves
            
            min_height = min(height)
            idx = height.index(min_height)
            ridx = idx + 1
            while ridx < m and height[ridx] == min_height:
                ridx += 1
            for i in range(min(ridx - idx, n - min_height), 0, -1):
                t = moves + 1 + len(set(h for h in height if h < n))
                heapq.heappush(q, (t, moves + 1, -i, height))
        '''
        '''
        total_area = m * n
        dp = [0] * (total_area + 1) 
        for i in range(1, total_area + 1):
            dp[i] = 1 + min(dp[i - k ** 2] for k in range(1, int(i ** 0.5) + 1))
        
        height = [0] * m
        q = []
        for i in range(min(m, n), 0, -1):
            heapq.heappush(q, (1 + dp[total_area - i ** 2], 1, i, height))
        
        while q:
            guess, moves, size, height = heapq.heappop(q)
            
            idx = height.index(min(height))
            height = height[:]
            for i in range(size):
                height[idx + i] += size   
            if all(h == n for h in height):
                return moves
            
            min_height = min(height)
            idx = height.index(min_height)
            ridx = idx + 1
            while ridx < m and height[ridx] == min_height:
                ridx += 1
            for i in range(min(ridx - idx, n - min_height), 0, -1):
                guess = dp[total_area - sum(height) - i ** 2]
                heapq.heappush(q, (guess + 1 + moves, moves + 1, i, height))
        '''
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
