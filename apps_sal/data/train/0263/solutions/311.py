class Solution:

    def knightDialer(self, n: int) -> int:
        neighbours = {1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (3, 9, 0), 5: tuple(), 6: (1, 7, 0), 7: (2, 6), 8: (1, 3), 9: (2, 4), 0: (4, 6)}
        memo = {}

        def helper(position, num_hops):
            if (position, num_hops) in memo:
                return memo[position, num_hops]
            if num_hops == 0:
                return 1
            num_sequences = 0
            for neighbour in neighbours[position]:
                num_sequences += helper(neighbour, num_hops - 1)
            memo[position, num_hops] = num_sequences
            return num_sequences
        total = 0
        for pos in neighbours:
            total += helper(pos, n - 1)
        return total % (10 ** 9 + 7)
