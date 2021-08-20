class Solution:

    def knightDialer(self, N: int) -> int:
        res = [1] * 10
        next_move = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        i = 1
        while i < N:
            res2 = [0] * 10
            for (k, v) in enumerate(res):
                for j in next_move[k]:
                    res2[j] += v
            res = res2
            i += 1
        return sum(res) % (10 ** 9 + 7)
