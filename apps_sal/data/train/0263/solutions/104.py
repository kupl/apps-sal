'''
'''


class Solution:
    def knightDialer(self, n: int) -> int:
        adj_lists = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]  # adj_lists[i] are the neighbors of digit i
        table = [[1] * 10 for i in range(n)]  # table[n][digit] is the number of solutions for length `n+1` starting at digit
        # table is already initialized for n=1

        for n0 in range(1, n):
            for digit in range(10):
                acc = 0
                for adj in adj_lists[digit]:
                    acc += table[n0 - 1][adj]
                table[n0][digit] = acc

        return sum(table[n - 1]) % (10**9 + 7)
