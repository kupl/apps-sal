class Solution:

    def distinctEchoSubstrings(self, text: str) -> int:

        def check(s):
            return s[:len(s) // 2] == s[len(s) // 2:]
        ret = set()
        n = len(text)
        for l in range(2, n + 1, 2):
            for start in range(n - l + 1):
                s = text[start:start + l]
                if check(text[start:start + l]):
                    ret.add(s)
        return len(ret)
