class Solution(object):
    def knightDialer(self, N):
        # Use This Code
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [],
                 [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        MOD = 10**9 + 7

        table = [1] * 10  # table[i] = number of way ending in i
        for _ in range(N - 1):
            temp = [0] * 10
            for node, count in enumerate(table):
                for nei in moves[node]:
                    temp[nei] += count
                    temp[nei] % MOD
            table = temp

        return sum(table) % MOD
