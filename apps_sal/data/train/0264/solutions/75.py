class Solution:

    def is_unique(self, word):
        letters = set()

        for letter in word:
            if letter in letters:
                return False
            letters.add(letter)
        return True

    def maxLength(self, arr: List[str]) -> int:

        uniques = set()

        for piece in arr:
            next_uniques = set()
            for unique in uniques:
                concat = piece + unique
                if self.is_unique(concat):
                    next_uniques.add(concat)
            if self.is_unique(piece):
                next_uniques.add(piece)
            for u in next_uniques:
                uniques.add(u)

        if uniques:
            return max([len(x) for x in uniques])
        return 0
