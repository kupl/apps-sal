class Solution:
    def knightDialer(self, n: int) -> int:

        dialer_map = {0: [4, 6],
                      1: [6, 8],
                      2: [7, 9],
                      3: [4, 8],
                      4: [0, 3, 9],
                      5: [],
                      6: [0, 1, 7],
                      7: [2, 6],
                      8: [1, 3],
                      9: [2, 4]}

        level = [1 for i in range(10)]

        for i in range(1, n):
            next_level = [0 for i in range(10)]
            for l in range(10):
                for d in dialer_map[l]:
                    next_level[d] += level[l]

            level = next_level

        return sum(level) % (10**9 + 7)
