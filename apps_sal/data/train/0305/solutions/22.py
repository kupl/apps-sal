class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        if n <= 1:
            return 0

        res = set()
        for i in range(n - 1):
            for j in range(min(i + 1, n - i - 1)):
                if text[(i - j):(i + 1)] == text[(i + 1):(i + j + 2)]:
                    res.add(text[(i - j):(i + j + 2)])

        return len(res)
