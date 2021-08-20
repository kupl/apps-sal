class Solution:

    def knightDialer(self, n: int) -> int:
        M = 10 ** 9 + 7
        current_ways = [1] * 10
        for i in range(1, n):
            prev = current_ways.copy()
            current_ways[0] = (prev[4] + prev[6]) % M
            current_ways[1] = (prev[6] + prev[8]) % M
            current_ways[2] = (prev[7] + prev[9]) % M
            current_ways[3] = (prev[4] + prev[8]) % M
            current_ways[4] = (prev[3] + prev[9] + prev[0]) % M
            current_ways[5] = 0
            current_ways[6] = (prev[1] + prev[7] + prev[0]) % M
            current_ways[7] = (prev[2] + prev[6]) % M
            current_ways[8] = (prev[1] + prev[3]) % M
            current_ways[9] = (prev[2] + prev[4]) % M
        return sum(current_ways) % M
