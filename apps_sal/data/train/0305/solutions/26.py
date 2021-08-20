class Solution:

    def distinctEchoSubstrings(self, text: str) -> int:
        s = text
        n = len(s)
        s += '.'
        some_string = set()
        for k in range(1, n // 2 + 1):
            same = sum((c == d for (c, d) in zip(s, s[k:k + k])))
            for i in range(n - 2 * k + 1):
                if same == k:
                    some_string.add(s[i:i + k])
                same += (s[i + k] == s[i + k + k]) - (s[i] == s[i + k])
        return len(some_string)
