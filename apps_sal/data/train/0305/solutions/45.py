class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:

        d = set()
        c = 0
        lim = len(text)

        for i in range(0, lim, 2):
            for j in range(0, lim - i):
                val = text[j:j + i]
                if val not in d:
                    d.add(val)
                    if 2 * val[:i // 2] == val:
                        c += 1
        if 2 * text[:lim // 2] == text:
            c += 1
        return c - 1
