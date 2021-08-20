class Solution:

    def numWays(self, s: str) -> int:
        m = 10 ** 9 + 7
        c = Counter(s)
        ones = c['1']
        if ones % 3 != 0:
            return 0
        if ones == 0:
            return comb(len(s) - 1, 2) % m
        count = 0
        a = 0
        b = 0
        for i in range(len(s)):
            if count == ones // 3:
                a += 1
            if count == 2 * ones // 3:
                b += 1
            if s[i] == '1':
                count += 1
        return a * b % m
