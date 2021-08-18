class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        s, n = text + '
        echo = set()
        for k in range(1, n // 2 + 1):
            same = sum(x == y for x, y in zip(s[:k], s[k:(k + k)]))
            for i in range(n - 2 * k + 1):
                if same == k:
                    echo.add(s[i:(i + 2 * k)])
                same += (s[i + k] == s[i + k + k]) - (s[i] == s[i + k])
        return len(echo)
