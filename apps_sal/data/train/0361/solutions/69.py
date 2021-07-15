class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if m > n: n, m = m, n
        res, state = m * n, [0] * n
        visited = {}
        def dfs(count):
            nonlocal res
            s = ''.join(str(v) for v in state)
            if s in visited and count > visited[s]:
                return
            visited[s] = count
            if count > res: return
            min_h = min(state)
            if min_h == m:
                res = min(res, count)
                return
            e = s = state.index(min_h)
            while e < n and state[e] == min_h:
                e += 1
            max_len = min(e - s, m - min_h)
            for l in range(max_len, 0, -1):
                for i in range(s, s + l):
                    state[i] += l
                dfs(count + 1)
                for i in range(s, s + l):
                    state[i] -= l
        dfs(0) 
        
        return res

