"""
"""


class Solution:

    def knightDialer(self, n: int) -> int:
        adj_lists = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        table = [[1] * 10 for i in range(n)]
        for n0 in range(1, n):
            for digit in range(10):
                acc = 0
                for adj in adj_lists[digit]:
                    acc += table[n0 - 1][adj]
                table[n0][digit] = acc
        return sum(table[n - 1]) % (10 ** 9 + 7)
