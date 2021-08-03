class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        res = set()
        for i in range(n):
            for j in range(i):
                if text[i] == text[j] and text.startswith(text[j:i], i):
                    res.add(text[j:i])
        return len(res)
