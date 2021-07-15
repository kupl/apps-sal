class Solution:
    def __init__(self):
        self.res = set()
        
    def backtrack(self,tiles,curr,indices):
        
        for i in range(len(tiles)):
            if i not in set(indices):
                curr+=tiles[i]
                indices.append(i)
                self.res.add(curr)
                
                if len(curr)<len(tiles):
                    self.backtrack(tiles,curr,indices)
                curr = curr[:-1]
                indices.pop()
                
                
        
        
    def numTilePossibilities(self, tiles: str) -> int:
        
        self.backtrack(tiles,'',[])
        
        return len(self.res)
