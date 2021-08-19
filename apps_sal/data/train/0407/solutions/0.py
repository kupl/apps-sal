class Solution:

    def scoreOfParentheses(self, S: str) -> int:
        (ans, val) = (0, 1)
        for i in range(len(S) - 1):
            if S[i:i + 2] == '((':
                val *= 2
            if S[i:i + 2] == '()':
                ans += val
            if S[i:i + 2] == '))':
                val //= 2
        return ans
