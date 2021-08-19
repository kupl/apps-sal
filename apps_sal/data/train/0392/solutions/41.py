class Solution:

    def numWays(self, s: str) -> int:
        ones = s.count('1')
        if ones % 3:
            return 0
        if ones == 0:
            return (len(s) - 1) * (len(s) - 2) // 2 % 1000000007
        ones //= 3
        c = 0
        (F, S) = (0, 0)
        for (i, x) in enumerate(s):
            if x == '1':
                c += 1
            if c == ones and x == '0':
                F += 1
            elif c == 2 * ones and x == '0':
                S += 1
        return (F + 1) * (S + 1) % 1000000007
