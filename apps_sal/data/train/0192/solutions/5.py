class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        rounds = []
        piles.sort()
        for i in range(int(len(piles) / 3)):
            round_draw = []
            round_draw.append(piles[i])
            round_draw.append(piles[-i * 2 - 2])
            round_draw.append(piles[-i * 2 - 1])
            rounds.append(round_draw)
        sum = 0
        for round_draw in rounds:
            sum += round_draw[1]
        return sum
