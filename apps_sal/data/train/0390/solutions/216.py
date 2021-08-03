class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        to_ret = [False]
        for i in range(1, n + 1):
            for j in range(int(i**0.5), 0, -1):
                if not to_ret[i - j * j]:
                    to_ret.append(True)
                    break
            if len(to_ret) == i:
                to_ret.append(False)
        return to_ret[-1]
