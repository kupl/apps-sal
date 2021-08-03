class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 10

        pad = {
            0: (4, 6),
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (0, 3, 9),
            5: tuple(),
            6: (0, 1, 7),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4),
        }

        current = [0] * 10
        prev = [1] * 10

        for _ in range(n - 1):
            current = [0] * 10

            for key in range(10):
                for bro in pad[key]:
                    current[key] += prev[bro]
            prev = current

        return sum(current) % (10**9 + 7)
