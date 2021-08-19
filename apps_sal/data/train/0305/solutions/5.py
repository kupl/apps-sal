class Solution:

    def distinctEchoSubstrings(self, text: str) -> int:

        def pos(s):
            n = len(s)
            if n % 2 != 0:
                return False
            for i in range(n // 2):
                if s[i] != s[i + n // 2]:
                    return False
            return True
        res = set()
        for i in range(len(text) - 1):
            for j in range(i + 1, len(text), 2):
                m = i + (j - i + 1) // 2
                if hash(text[i:m]) == hash(text[m:j + 1]):
                    res.add(text[i:m])
        return len(res)
