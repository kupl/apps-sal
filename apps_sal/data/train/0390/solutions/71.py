class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        l = [1]
        pos = [0] * (n + 1)
        for i in range(1, n + 1):
            if i == (math.sqrt(l[-1]) + 1) ** 2:
                l.append(int((math.sqrt(l[-1]) + 1) ** 2))
            for square_num in l:
                if not pos[i - square_num]:
                    pos[i] = 1
        return pos[n]
