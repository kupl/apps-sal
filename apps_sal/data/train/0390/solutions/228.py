class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        ans_list = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, int(i**0.5) + 1):
                if ans_list[i - j * j] == 0:
                    ans_list[i] = 1
                    break
        # print(ans_list)
        return ans_list[-1]
