class Solution:

    def distinctEchoSubstrings(self, text: str) -> int:
        return len({text[a:a + b] for a in range(len(text) - 1) for b in range(1, (len(text) - a) // 2 + 1) if text[a:a + b] == text[a + b:a + 2 * b]})
