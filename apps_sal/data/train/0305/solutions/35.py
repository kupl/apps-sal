class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        # O(N^2) check all substr, O(1) each check with rolling count of equality
        # s: text + '#' in case length of text is odd and out of index error
        s, n = text + '#', len(text)
        echo = set()
        for k in range(1, n // 2 + 1):
            # init
            same = sum(x == y for x, y in zip(s[:k], s[k:(k + k)]))
            for i in range(n - 2 * k + 1):
                if same == k:
                    echo.add(s[i:(i + 2 * k)])
                # rolling the count of equality
                same += (s[i + k] == s[i + k + k]) - (s[i] == s[i + k])
        return len(echo)
