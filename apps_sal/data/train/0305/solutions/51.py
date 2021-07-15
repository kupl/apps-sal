class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        seen = set()
        for i in range(n):
            for j in range(i + 1, n + 1):
                if not (j - i) % 2 and text[i: i + (j - i) // 2] == text[i + (j - i) // 2: j]:
                    seen.add(text[i: j])
        return len(seen)
