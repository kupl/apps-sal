class Solution:

    def minAddToMakeValid(self, S: str) -> int:
        if not S:
            return 0
        N = len(S)
        open_brackets = [0] * N
        close_brackets = [0] * N
        ans = 0
        for (i, c) in enumerate(S):
            if i > 0:
                open_brackets[i] = open_brackets[i - 1]
                close_brackets[i] = close_brackets[i - 1]
            if c == '(':
                open_brackets[i] += 1
            elif c == ')':
                close_brackets[i] += 1
            if close_brackets[i] > open_brackets[i]:
                diff = close_brackets[i] - open_brackets[i]
                ans += diff
                open_brackets[i] += diff
        return ans + open_brackets[-1] - close_brackets[-1]
