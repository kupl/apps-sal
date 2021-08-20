def is_winning(n):
    winning = []
    for val in range(0, n + 1):
        if val == 0:
            ans = False
        else:
            ans = False
            i = 1
            while val - i * i >= 0:
                if not winning[val - i * i]:
                    ans = True
                    break
                i += 1
        winning.append(ans)
    return winning[n]


class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        return is_winning(n)
