class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        self._visited = {}
        alex_minus_lee = self.search(piles, 0, len(piles) - 1)
        return alex_minus_lee > 0

    def search(self, piles: List[int], start: int, end: int):
        if start > end:
            return 0
        key = (start, end)
        if key in self._visited:
            return self._visited[key]

        score = max(piles[start] - self.search(piles, start + 1, end),
                    piles[end] - self.search(piles, start, end - 1))

        self._visited[key] = score

        return score
