class Solution:

    def numWays(self, s: str) -> int:
        ones = 0
        zeroes = 0
        for char in s:
            if char == '1':
                ones += 1
            else:
                zeroes += 1
        if ones > 0 and ones % 3 != 0:
            return 0
        if ones == 0:
            n = len(s) - 3
            res = 1
            diff = 2
            while n:
                res += diff
                diff += 1
                n -= 1
            return res % (10 ** 9 + 7)
        ones_interval = ones // 3
        (left, right) = (0, 0)
        i = 0
        temp = 0
        while i < len(s):
            if s[i] == '1':
                temp += 1
            i += 1
            if temp == ones_interval:
                break
        while i < len(s):
            if s[i] == '0':
                left += 1
            if s[i] == '1' or temp == 2 * ones_interval:
                break
            i += 1
        while i < len(s):
            if s[i] == '1':
                temp += 1
            i += 1
            if temp == 2 * ones_interval:
                break
        while i < len(s):
            if s[i] == '0':
                right += 1
            if s[i] == '1':
                break
            i += 1
        if not left:
            return (right + 1) % (10 ** 9 + 7)
        if not right:
            return (left + 1) % (10 ** 9 + 7)
        return (left + 1) * (right + 1) % (10 ** 9 + 7)
