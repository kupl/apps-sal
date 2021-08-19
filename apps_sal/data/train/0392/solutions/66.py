class Solution:
    CONST = 1000000000 + 7

    def numWays(self, s: str) -> int:
        n = len(s)
        num_ones = 0
        for c in s:
            if c == '1':
                num_ones += 1
        if num_ones % 3 != 0:
            return 0
        if num_ones == 0:
            return (n - 1) * (n - 2) // 2 % self.CONST
        num_ones_per_chunk = num_ones // 3
        (first, second) = (0, 0)
        num_ones_sofar = 0
        for (idx, c) in enumerate(s):
            num_ones_sofar += c == '1'
            if num_ones_sofar < num_ones_per_chunk:
                pass
            elif num_ones_per_chunk <= num_ones_sofar < num_ones_per_chunk + 1:
                first += 1
            elif 2 * num_ones_per_chunk <= num_ones_sofar < 2 * num_ones_per_chunk + 1:
                second += 1
            else:
                pass
        return first * second % self.CONST
