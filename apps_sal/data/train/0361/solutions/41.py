class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n>m:
            n, m = m, n
        res, memo = n*m, [math.inf] * (n*m + 1)
        memo[0] = 0
        
        def dfs(heights, count, rem_area):
            nonlocal res
            if count >= res:
                return math.inf
            if memo[rem_area]!=math.inf and count + memo[rem_area] >= res:
                return math.inf
            
            lowest_idx, lowest_height, width, prev = -1, math.inf, 0, -1
            for i in range(m):
                if heights[i] < lowest_height:
                    lowest_height, lowest_idx, width, prev = heights[i], i, 1, i
                elif heights[i] == lowest_height and prev == i-1:
                    width, prev = width + 1, i
            
            if rem_area == 0:
                res = min(res, count)
                return 0
            
            min_count, width = math.inf, min(width, n-lowest_height)
            for w in range(width, 0, -1):
                temp = heights.copy()
                for j in range(lowest_idx, lowest_idx+w):
                    temp[j] += w
                min_count = min(min_count, dfs(temp, count+1, rem_area - w*w))
            memo[rem_area] = min(memo[rem_area], min_count)
            return min_count
        
        dfs([0]*m, 0, n*m)
        return res

