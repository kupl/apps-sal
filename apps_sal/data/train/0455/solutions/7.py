from collections import defaultdict
class Solution:
    def all_same(self, left, right, bottom, top, color):
        for i in range(bottom, top+1):
            for j in range(left, right+1):
                if self.grid[i][j] and self.grid[i][j] != color:
                    return False
        return True
    
    def fill(self, left, right, bottom, top):
        for i in range(bottom, top+1):
            for j in range(left, right+1):
                self.grid[i][j] = 0
                
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        self.rect = defaultdict(lambda : [10**9, -10**9, 10**9, -10**9])
        for i, row in enumerate(targetGrid):
            for j, color in enumerate(row):
                self.rect[color][0] = min(self.rect[color][0], j)
                self.rect[color][1] = max(self.rect[color][1], j)
                self.rect[color][2] = min(self.rect[color][2], i)
                self.rect[color][3] = max(self.rect[color][3], i)
        self.grid = targetGrid
        while self.rect:
            for color in self.rect:
                left, right, bottom, top = self.rect[color]
                if self.all_same(left, right, bottom, top, color):
                    self.fill(left, right, bottom, top)
                    self.rect.pop(color)
                    break
            else:         
                return False
        return True
