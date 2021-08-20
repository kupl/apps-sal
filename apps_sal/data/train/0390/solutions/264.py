class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        result = []
        result.append(False)
        for i in range(1, n + 1):
            j = 1
            flag = True
            while j * j <= i:
                if not result[i - j * j]:
                    flag = False
                    break
                j += 1
            if flag == True:
                result.append(False)
            else:
                result.append(True)
        print(result)
        return result[-1]
