class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        arr = [0] * (n + 1)
        arr[0] = False
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                square = j * j
                if square > i:
                    break
                elif square == i:
                    arr[i] = True
                    break
                else:
                    rest = i - square
                    if arr[rest] == False:
                        arr[i] = True
                        break
        return arr[n]
