class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        tile_counts = collections.Counter(tiles)
        len_counts = [1] + [0] * len(tiles)
        for tile in tile_counts:
            new_len_counts = [0] * (len(tiles) + 1)
            num_tiles = tile_counts[tile]
            for num_inserted in range(num_tiles + 1):
                for (old_len, old_len_count) in enumerate(len_counts):
                    new_len = old_len + num_inserted
                    if new_len > len(tiles):
                        break
                    num_patterns = math.comb(new_len, num_inserted)
                    new_len_counts[new_len] += old_len_count * num_patterns
            len_counts = new_len_counts
        return sum(len_counts) - 1
