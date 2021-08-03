from math import factorial


class Solution:
    def numWays(self, s: str) -> int:
        count1 = s.count('1')
        if count1 % 3 != 0:
            return 0
        required = s.count('1') // 3
        if not required:
            return (factorial(len(s) - 1) // factorial(len(s) - 3) // 2) % 1000000007

        options = 1
        for loop in range(2):
            current = 0
            for i, ch in enumerate(s):
                if current == required:
                    break
                if ch == '1':
                    current += 1
            for j, ch in enumerate(s[i:], 1):
                if ch == '1':
                    break
            options *= j
            s = s[::-1]

        return options % 1000000007
