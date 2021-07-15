class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        return len(set(x for i in range(1,len(tiles)+1) for x in itertools.permutations(tiles,i)))
        

