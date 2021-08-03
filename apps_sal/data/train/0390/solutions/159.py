class Solution:

    table = [-1] * 1000001
    table[0] = False
    table[1] = True
    idx = 1

    def winnerSquareGame(self, n: int) -> bool:

        if n > self.idx:
            for i in range(self.idx + 1, n + 1):
                num = 1
                while num ** 2 <= i:
                    square = num ** 2
                    if not self.table[i - square]:
                        self.table[i] = True
                        break
                    num += 1
                if self.table[i] == -1:
                    self.table[i] = False
            self.idx = i
        return self.table[n]
