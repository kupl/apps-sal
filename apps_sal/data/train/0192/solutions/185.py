class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        asc = sorted(piles)
        desc = sorted(piles, reverse=True)
        new = []
        for i in range(len(piles) // 3):
            new.append(asc.pop())
            new.append(asc.pop())
            new.append(desc.pop())
        return sum([new[i] for i in range(len(new)) if i % 3 == 1])
