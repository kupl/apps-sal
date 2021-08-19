class Solution:

    def distinctEchoSubstrings(self, text: str) -> int:
        out = set()
        for i in range(len(text) - 1):
            for j in range(i + 1, len(text)):
                if text[i:j] == text[j:2 * j - i]:
                    out.add(text[i:j])
        return len(out)
