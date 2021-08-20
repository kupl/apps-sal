from collections import Counter


class Solution:

    def __init__(self):
        self.sum_ = 0

    def recurse_count(self, letter_count):
        if len(letter_count) == 0:
            return
        for letter in letter_count:
            self.recurse_count(letter_count - Counter(letter))
            self.sum_ += 1
        return

    def numTilePossibilities(self, tiles: str) -> int:
        letter_count = Counter(tiles)
        self.recurse_count(letter_count)
        return self.sum_
