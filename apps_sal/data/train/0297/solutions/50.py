class Solution:

    def numTilePossibilities(self, tiles: str) -> int:

        def backtrack(i, c):
            if i == n:
                return
            for k in c:
                if c[k] > 0:
                    self.ans += 1
                    backtrack(i + 1, c - Counter(k))
        n = len(tiles)
        counter = Counter(tiles)
        self.ans = 0
        backtrack(0, counter)
        return self.ans
