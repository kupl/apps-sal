class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        text += '.'
        seen = set()
        for k in range(1, n // 2 + 1):
            same = sum(c == d for c, d in zip(text, text[k: k + k]))
            for i in range(n - 2 * k + 1):
                if same == k:
                    seen.add(text[i: i + k])
                same += (text[i + k] == text[i + k * 2]) - (text[i] == text[i + k])
        return len(seen)
