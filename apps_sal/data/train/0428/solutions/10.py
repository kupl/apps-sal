class Solution:

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        keylock = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f'}
        m = len(grid)
        n = len(grid[0])
        keys_target = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                elif grid[i][j] in 'abcdef':
                    keys_target = keys_target | 1 << keylock[grid[i][j]]

        def keyAllAcquired(value):
            if value & keys_target == keys_target:
                return True
            else:
                return False

        def isMovable(i, j):
            if 0 <= i <= m - 1 and 0 <= j <= n - 1 and (grid[i][j] != '#'):
                return True
            else:
                return False
        visited_states = {(start, 0)}
        q = collections.deque()
        q.append((start, 0))
        step = 0
        while q:
            q_len = len(q)
            for _ in range(q_len):
                ((i, j), keys) = q.popleft()
                if keyAllAcquired(keys):
                    return step
                directs = [-1, 0, 1, 0, -1]
                for d in range(4):
                    newi = i + directs[d]
                    newj = j + directs[d + 1]
                    if isMovable(newi, newj):
                        if grid[newi][newj] in 'abcdef':
                            new_state = ((newi, newj), keys | 1 << keylock[grid[newi][newj]])
                            if new_state not in visited_states:
                                visited_states.add(new_state)
                                q.append(new_state)
                        elif grid[newi][newj] in 'ABCDEF':
                            lower_int = keylock[keylock[grid[newi][newj]]]
                            new_state = ((newi, newj), keys | 1 << lower_int + 6)
                            if keys & 1 << lower_int and new_state not in visited_states:
                                visited_states.add(new_state)
                                q.append(new_state)
                        elif grid[newi][newj] in '.@' and ((newi, newj), keys) not in visited_states:
                            visited_states.add(((newi, newj), keys))
                            q.append(((newi, newj), keys))
            step += 1
        return -1
