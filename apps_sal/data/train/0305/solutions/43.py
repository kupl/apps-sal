class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        L = len(text)
        res = set()
        for i in range(1, L):
            for j in range(max(0, 2 * i - L), i):
                if text[j:i] == text[i:2 * i - j]:
                    res.add(text[j:i])
        return len(res)
