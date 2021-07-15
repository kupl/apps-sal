class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        words = set()
        curr = ''
        tile_count = {}
        for x in tiles:
            if x not in tile_count:
                tile_count[x] = 0
            tile_count[x] += 1
        
        def walk(curr, tiles, words):
            #print(tiles, curr)
            for tile in tiles:
                if tiles[tile] > 0:
                    temp = curr + tile
                    #print('Temp', temp)
                    temp_tiles = tiles.copy()
                    temp_tiles[tile] -= 1
                    words.add(temp)
                    walk(temp, temp_tiles, words)
        for tile in tile_count:
            walk('', tile_count, words)
        return len(words)
