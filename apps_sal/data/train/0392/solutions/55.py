class Solution:

    def numWays(self, s: str) -> int:
        c = s.count('1')
        if c % 3:
            return 0
        M = 10 ** 9 + 7
        if not c:
            return (len(s) - 1) * (len(s) - 2) // 2 % M
        cur = 0
        first = 0
        second = 0
        for l in s:
            if cur == c // 3:
                first += 1
            elif cur == c // 3 * 2:
                second += 1
            cur += l == '1'
        return first * second % M
