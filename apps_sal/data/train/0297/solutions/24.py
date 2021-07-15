class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtracking(idx=0,seq='',remaining=tiles):
            for i, tile in enumerate(remaining):
                res.add(seq+tile)
                backtracking(idx+1, seq+tile, remaining[:i]+remaining[i+1:])
                
        res = set()
        backtracking()
        return len(res)
