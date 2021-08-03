class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = set()
        maxx = len(tiles)

        def dfs(result, tiles, current_sequence=''):
            if current_sequence != '':
                result.add(current_sequence)
            for t in tiles:
                tiles_c = tiles.replace(t, '', 1)
                dfs(result, tiles_c, current_sequence + t)
        dfs(result, tiles)
        return len(result)
