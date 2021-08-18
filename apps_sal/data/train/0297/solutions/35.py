class Solution:

    def make_tile(self, curr, used, letters, size):

        if len(curr) == size:

            self.res += 1

            return

        i = 0

        while i < len(letters):

            if i not in used:

                used.add(i)

                curr.append(letters[i])

                self.make_tile(curr, used, letters, size)

                curr.pop(-1)

                used.remove(i)

                while i + 1 < len(letters) and letters[i] == letters[i + 1]:

                    i += 1

            i += 1

    def numTilePossibilities(self, tiles: str) -> int:

        self.res = 0

        letters = sorted(tiles)

        for size in range(1, len(tiles) + 1):

            self.make_tile([], set(), letters, size)

        return self.res
