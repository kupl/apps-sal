class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        res = set()
        mem = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n - 1):
                mem[i][preferences[i][j]] = j + 1

        for i in range(n // 2):
            x = pairs[i][0]
            y = pairs[i][1]
            for j in range(i + 1, n // 2):
                u = pairs[j][0]
                v = pairs[j][1]
                if mem[x][u] < mem[x][y] and mem[u][x] < mem[u][v]:
                    res.add(x)
                    res.add(u)
                if mem[x][v] < mem[x][y] and mem[v][x] < mem[v][u]:
                    res.add(x)
                    res.add(v)
                if mem[y][u] < mem[y][x] and mem[u][y] < mem[u][v]:
                    res.add(y)
                    res.add(u)
                if mem[y][v] < mem[y][x] and mem[v][y] < mem[v][u]:
                    res.add(y)
                    res.add(v)

        return len(res)
