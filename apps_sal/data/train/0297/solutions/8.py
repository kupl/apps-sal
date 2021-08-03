class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        combination_set = self.generateTilePossibilities(tiles)
        return len(combination_set)

    def generateTilePossibilities(self, tiles: str):
        n = len(tiles)
        combination_set = set()
        for index in range(n):
            combination_set.add(tiles[index])
        if n > 1:
            for index in range(n):
                tiles_without_n = tiles[0:index] + tiles[index + 1:]
                additional_combinations = self.generateTilePossibilities(
                    tiles_without_n)
                combination_set.add(tiles_without_n)
                for combination in additional_combinations:
                    combination_set.add(combination)
                    for second_index in range(len(combination)):
                        new_tile_combination = combination[
                            0:second_index] + tiles[index] + combination[
                                second_index:]
                        combination_set.add(new_tile_combination)
        return combination_set
