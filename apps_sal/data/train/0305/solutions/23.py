class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        res = set()
        for length in range(1, 1 + len(text) // 2):
            count = 0
            l, r = 0, length
            while r < len(text):
                if text[l] == text[r]:
                    count += 1
                else:
                    count = 0
                if count == length:
                    res.add(text[l - length + 1: l + 1])
                    count -= 1
                l, r = l + 1, r + 1
        return len(res)
