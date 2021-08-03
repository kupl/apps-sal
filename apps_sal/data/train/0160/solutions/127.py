class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        payoffs = piles
        r = 1
        while len(payoffs) > 1:
            new_payoffs = []
            for i in range(len(payoffs) - 1):
                new_payoffs.append(max(piles[i] - payoffs[i + 1], piles[i + r] - payoffs[i]))
            payoffs = new_payoffs
            r += 1
        return payoffs[0] > 0
