#[Runtime: 452 ms, faster than 97.27%] Hash
#O(MN)
#1. traverse all cells and mark server as (x, y)
#2. put each server (x, y) into serveral bucket named x1, x2, .., and y1, y2, ..
# e.g. each xbucket[x1] maintains the number of servers on line x1
#3. enumerate all server (x', y'), and see if there is at least 2 server on xbucket[x'] or ybucket[y'] 
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        xbucket, ybucket, server = [0] * len(grid), [0] * len(grid[0]), []
        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if cell:
                    server.append((x, y))
                    xbucket[x] += 1
                    ybucket[y] += 1
        return sum(xbucket[x] > 1 or ybucket[y] > 1 for x, y in server)
