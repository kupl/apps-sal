class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        mem = dict()

        def search(i, j):
            if i > j:
                return 0
            if (i, j) in mem:
                return mem.get((i, j))
            side = (j - i + 1) % 2
            if side == 0:
                ret = max(search(i + 1, j) + piles[i], search(i, j - 1) + piles[j])
                mem[i, j] = ret
                return ret
            else:
                ret = min(search(i + 1, j) - piles[i], search(i, j - 1) - piles[j])
                mem[i, j] = ret
                return ret
        return search(0, len(piles) - 1) > 0
