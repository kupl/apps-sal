class Solution:
    CONST = 10**9 + 7

    def numWays(self, s: str) -> int:
        n = len(s)
        num_ones = 0
        for c in s:
            if c == '1':
                num_ones += 1
        if num_ones % 3 != 0:
            return 0
        if num_ones == 0:
            return ((n - 1) * (n - 2) // 2) % self.CONST

        first, second = 0, 0
        num_ones_sofar, cutoff = 0, num_ones // 3
        for i in range(n):
            num_ones_sofar += s[i] == '1'
            if num_ones_sofar < cutoff:
                pass
            elif cutoff <= num_ones_sofar < cutoff + 1:
                first += 1
            elif 2 * cutoff <= num_ones_sofar < 2 * cutoff + 1:
                second += 1
            else:
                pass
        return (first * second) % self.CONST
