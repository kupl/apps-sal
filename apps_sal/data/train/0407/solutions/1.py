class Solution:

    def scoreOfParentheses(self, S: str) -> int:

        def h(i, j):
            if i > j:
                return 0
            c = 0
            ki = i
            x = 0
            for k in range(i, j + 1):
                c += 1 if S[k] == '(' else -1
                if c == 0:
                    x += max(1, 2 * h(ki + 1, k - 1))
                    ki = k + 1
            return x
        return h(0, len(S) - 1)
