class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        self.dic = {}
        self.length = len(piles)

        def search(i, j):
            if i > j:
                return 0
            if (i, j) in self.dic:
                return self.dic.get((i, j))
            parity = (j - i + 1) % 2
            if parity == 0:
                ret1 = max(piles[i] + search(i + 1, j), piles[j] + search(i, j - 1))
                self.dic[i, j] = ret1
                return ret1
            else:
                ret2 = min(-piles[i] + search(i + 1, j), -piles[j] + search(i, j - 1))
                self.dic[i, j] = ret2
                return ret2
        return search(0, self.length - 1) > 0
