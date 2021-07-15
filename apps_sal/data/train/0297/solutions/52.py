def possible(tiles):
    variants = set()
    if len(tiles) == 1:
        variants.add(tiles[0])
    else:
        for i in range(len(tiles)):
            t = possible(tiles[:i]+tiles[i+1:])
            variants.update(t)
            for j in t:
                variants.add(tiles[i]+j)
    return variants
    

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return len(possible(tiles))
        
            

