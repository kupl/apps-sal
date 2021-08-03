class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        if len(piles) == 0:
            return False
        ans = []
        l = len(piles)
        for i in range(l):
            ans.append(max(piles[0], piles[-1]))
            piles.remove(max(piles[0], piles[-1]))
            print(ans)
        if ans[-2] >= ans[-1]:
            return True
