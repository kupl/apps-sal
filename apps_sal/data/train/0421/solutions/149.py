class Solution:
    def lastSubstring(self, s: str) -> str:
        if not s:
            return s
        first, second, runner = 0, 1, 0
        while second + runner < len(s):
            if s[first + runner] == s[second + runner]:
                runner += 1
            elif s[first + runner] > s[second + runner]:
                second = second + runner + 1
                runner = 0
            else:
                if s[second + runner] > s[first]:
                    first, second, runner = second + runner, second + runner + 1, 0
                else:
                    first, second, runner = second, second + 1, 0

        return s[first:]
