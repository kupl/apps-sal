class Solution:
    def numWays(self, s: str) -> int:
        ones = 0
        d = {}
        for i in range(len(s)):
            x = s[i]
            if x == '1':
                ones += 1
            d[i] = ones
        if ones % 3 != 0:
            return 0
        if ones == 0:
            return (len(s) - 1) * (len(s) - 2) // 2 % (10**9 + 7)
        one = 0
        for i in range(len(s) - 2):
            if d[i] * 3 == ones:
                one += 1
            elif d[i] * 3 > ones:
                break
        two = 0
        for i in range(i, len(s) - 1):
            if (d[i] / 2) * 3 == ones:
                two += 1
            elif (d[i] / 2) * 3 > ones:
                break
        return (one * two) % (10**9 + 7)
