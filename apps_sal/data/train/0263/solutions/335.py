class Solution:
    def nextHops(self, row: int, col: int) -> list:
        hops = []
        if (row, col) not in self.hopDict:       
            for jump in [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2),(-1, 2), (-2, 1)]:
                nr, nc = row + jump[0], col + jump[1]
                if nr < 0 or nc < 0 or nr > 2 or nc > 2:
                    if (nr == 3 and nc == 1):
                        hops.append((nr, nc))
                    continue

                hops.append((nr, nc))
                
            self.hopDict[(row, col)] = hops
            
        return self.hopDict[(row, col)]
    
    def knightDialer(self, n: int) -> int:
        if n == 0:
             return
            
        reached = [ [1] * 3 for _ in range(4)]
        reached[3][0] = 0
        reached[3][2] = 0
        self.hopDict = {}

        for move in range(2, n + 1):
            nreached = [ [0] * 3 for _ in range(4)]
            for i, row in enumerate(reached):
                for j, button in enumerate(row):
                    if button == 0:
                        continue

                    for hop in self.nextHops(i, j):
                        nreached[hop[0]][hop[1]] += button
                        nreached[hop[0]][hop[1]] %= (10**9 + 7)
            
            reached = nreached
        
        return sum(map(sum, reached)) % (10**9 + 7)
