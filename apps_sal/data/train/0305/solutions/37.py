class Solution:

    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        res = set()
        for k in range(1, n // 2 + 1):
            for i in range(n - k + 1):
                if text[i:i + k] == text[i + k:i + 2 * k]:
                    res.add(text[i:i + 2 * k])
        return len(res)
