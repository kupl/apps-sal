class Solution:
    def knightDialer(self, n: int) -> int:
        num_map = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        table = [[0 for _ in range(10)] for _ in range(2)]
        for j in range(10):
            table[0][j] = 1

        for i in range(1, n):
            for j in range(10):
                sum_d = 0
                for d in num_map[j]:
                    sum_d += table[(i - 1) % 2][d]
                table[i % 2][j] = sum_d

        return sum(table[(n - 1) % 2]) % (1000000007)
