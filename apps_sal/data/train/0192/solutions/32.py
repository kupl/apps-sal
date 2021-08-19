class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        arr = sorted(piles)
        res = []
        n = len(piles) // 3
        while len(arr) > n:
            arr.pop(-1)
            res.append(arr.pop(-1))
        return sum(res)
