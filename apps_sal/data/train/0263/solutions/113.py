import logging

LOG = logging.getLogger(__name__)
MODULO = 10**9 + 7

class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        counts = [2, 2, 3, 2]
        for _ in range(n-2):
            next_counts = [
                (counts[1] + counts[2]),
                (2 * counts[0]),
                (2 * counts[0] + counts[3]),
                (2 * counts[2])
            ]

            counts= next_counts

        return (4 * counts[0] + 2 * counts[1]  + 2 * counts[2]  + counts[3]) % MODULO

