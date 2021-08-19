class Solution:

    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        res = 0
        for c in s:
            if c == '(':
                left += 1
            if c == ')':
                right += 1
            if left == right:
                res = max(res, left + right)
            if right > left:
                left = 0
                right = 0
        left = 0
        right = 0
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c == '(':
                left += 1
            if c == ')':
                right += 1
            if left == right:
                res = max(res, left + right)
            if left > right:
                left = 0
                right = 0
        return res
