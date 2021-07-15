from collections import deque
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        ## BFS search
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        m = len(grid)
        n = len(grid[0])
        visited = set()
        q = deque()
        cnt = 0
        ## find the starting point and count how many keys are there
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    q.append((i, j, 0))
                    visited.add((i, j, 0))
                elif grid[i][j] in 'abcdef':
                    cnt += 1
                    
        keys = set('abcdef')
        locks = set('ABCDEF')
        ## use bit mask to represent how many keys we have
        ## the target is to collect all keys, i.e, 2**(cnt)-1
        target = 2**(cnt)-1
        steps = 0
        while len(q)>0:
            q_sz = len(q)
            for _ in range(q_sz):
                x, y, cur_keys = q.popleft()
                if cur_keys == target:
                    return steps
                for d in dirs:
                    next_x, next_y = x+d[0], y+d[1]
                    pos_flag = False ## mark if the next position is legal
                    if 0<=next_x<m and 0<=next_y<n and grid[next_x][next_y] != '#':
                        new_keys = cur_keys
                        ## if the next position is a lock:
                        ## we must have its corresponding key to make a legal
                        ## otherwise, cannot reach next position
                        if grid[next_x][next_y] in locks:
                            lock = ord(grid[next_x][next_y]) - ord('A')
                            if (1<<lock) & cur_keys != 0:
                                pos_flag = True
                        ## if the next position is a key
                        elif grid[next_x][next_y] in keys:
                            key = ord(grid[next_x][next_y]) - ord('a')
                            new_keys = cur_keys | (1<<key) ## collect the key
                            pos_flag = True
                        else: ## the next position is '.'
                            pos_flag = True
                        ## only when the next position is legal
                        ## and we have not reach there with current keys,
                        ## we will reach there and search 
                        if pos_flag and (next_x, next_y, new_keys) not in visited:
                            visited.add((next_x, next_y, new_keys))
                            q.append((next_x, next_y, new_keys))
            steps += 1
        return -1
