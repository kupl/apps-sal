class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = []
        cols = []
        servers = []
        conn = 0
        i = 0
        while i < len(grid):
            j = 0
            while j < len(grid[i]):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
                    servers.append((i,j))
                j += 1
            i += 1
        for server in servers:
            if rows.count(server[0]) > 1 or cols.count(server[1]) > 1:
                conn += 1
        return conn
