class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def helper(curr, tiles):
            for i in range(len(tiles)):
                curr.append(tiles[i])
                pos.add(str(curr))
                c = tiles.copy()
                c.pop(i)
                helper(curr.copy(), c)
                curr.pop()
            
        tiles = list(tiles)
        pos = set()
                
        helper([], tiles)
        return len(pos)
        
                
            
            

