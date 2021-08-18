

class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        chessmap = {1: [4, 2], 2: [1, 3], 3: [4, 2], 4: [3, 1, 0], 0: [4, 4]}
        table = [1] * 5
        for i in range(2, n + 1):
            tmp = [0] * 5
            for j in range(5):
                for k in chessmap[j]:
                    tmp[j] += table[k]
            table = tmp
        return (sum(table) * 2 - table[0]) % (10**9 + 7)
