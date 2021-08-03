class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        a = 0
        b = len(piles) - 2
        c = len(piles) - 1
        count = 0
        while a < len(piles) and b > 0 and c > 0 and a < b and a < c:
            count += piles[b]
            a += 1
            c -= 2
            b -= 2
        print(count)
        return count
