import functools
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        # 谷歌面经。给定你一个矩形。问你最少需要多少个正方形来填满。
        '''
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
        '''
        '''
        self.res = m * n
        def dfs(height, moves):
            if all(h == n for h in height):
                self.res = min(self.res, moves)
            if moves >= self.res:  # 剪枝
                return 
            min_height = min(height)
            idx = height.index(min_height)
            ridx = idx + 1
            while ridx < m and height[ridx] == min_height:  # 找到了一个最大的范围
                ridx += 1
            for i in range(min(ridx - idx, n - min_height), 0, -1):
                new_height = height[:]
                for j in range(i):
                    new_height[idx + j] += i
                dfs(new_height, moves + 1)
        dfs([0] * m, 0)  # dfs的是目前的状态以及导致目前状态的操作步骤数
        return self.res
        '''
        '''
        # A* algrithm
        height = [0] * m
        q = []
        for i in range(min(m, n), 0, -1):
            # push to heap: (guess, moves, -size, height)
            heapq.heappush(q, (1, 1, -i, height)) # 这里的height是size还没用,待处理的
        
        while q:
            guess, moves, neg_size, height = heapq.heappop(q)
            size = -neg_size
            
            idx = height.index(min(height))  # 默认操作从左侧最低的位置装
            height = height[:]    # 如果最小堆tuple弹出里有数组，用的时候，先把数组全部取一下[:]
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
        dp = [0] * (total_area + 1) # 使用dp的方法去(猜测)目前最少需要多少个square填满
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
                height[idx + i] += size   #这里不能把i写成1
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
        # 仔细观察题目,可以发现其实一个矩形就是三种切法。横切竖切以及中间矩形分割。
        # 对于中间矩形分割，只要知道矩形的位置和大小，那么周围的四个矩形就可以求出来。
        @lru_cache(None)
        def dfs(i, j):
            # corner case
            if i == j:
                return 1
            if i == 1:
                return j
            if j == 1:
                return i
            
            res = i * j     # 最多也就x*y这么多个，作为最大值先赋res
            for x in range(1, i // 2 + 1):
                res = min(res, dfs(x, j) + dfs(i - x, j))
            for y in range(1, j // 2 + 1):
                res = min(res, dfs(i, y) + dfs(i, j - y))
            
            #https://blog.csdn.net/qq_17550379/article/details/102787329?ops_request_misc=&request_id=&biz_id=102&utm_term=leetcode%E9%93%BA%E7%93%B7%E7%A0%96&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0-102787329
            for leng in range(1, min(x, y)):  # 中间正方形的大小
                for x in range(1, i - leng):    # 正方形的左上角位置,保证不会贴合四个大边
                    for y in range(1, j - leng):
                        res = min(res, dfs(x + leng, y) + dfs(i - (x + leng), y + leng) + dfs(x, j - y) + dfs(i - x, j - (y + leng)) + 1)
            return res
        return dfs(m, n) # dfs矩形大小，用长宽两个变量来表示
