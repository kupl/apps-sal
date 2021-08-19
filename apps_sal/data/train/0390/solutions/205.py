class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        win = [False]
        for i in range(n):
            j = 1
            can_win = False
            while j ** 2 <= len(win):
                if not win[-j ** 2]:
                    can_win = True
                    break
                j += 1
            win.append(can_win)
        return win[-1]
