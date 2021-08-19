class Solution:

    def numWays(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        ones = 0
        for c in s:
            ones += 1 if c == '1' else 0
        n = len(s)
        if ones % 3 != 0:
            return 0
        if ones == 0:
            return (n - 2) * (n - 1) // 2 % MOD
        ones = ones // 3
        firstLeft = firstRight = -1
        secondLeft = secondRight = -1
        count = 0
        for i in range(n):
            if s[i] == '1':
                count += 1
            if count == ones and firstLeft == -1:
                firstLeft = i
            if count == ones + 1 and firstRight == -1:
                firstRight = i
            if count == 2 * ones and secondLeft == -1:
                secondLeft = i
            if count == 2 * ones + 1 and secondRight == -1:
                secondRight = i
        return (firstRight - firstLeft) * (secondRight - secondLeft) % MOD
