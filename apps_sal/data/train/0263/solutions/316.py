class Solution:

    def knightDialer(self, n: int) -> int:
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        cache = {}

        def backtrack(pos, hops):
            if (pos, hops) in cache:
                return cache[pos, hops]
            if hops == 0:
                return 1
            count = 0
            for nbr in moves[pos]:
                count += backtrack(nbr, hops - 1)
            cache[pos, hops] = count
            return count
        counts = 0
        for pos in range(10):
            counts += backtrack(pos, n - 1)
        return counts % (10 ** 9 + 7)
