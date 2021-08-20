class Solution:

    def distinctEchoSubstrings(self, text: str) -> int:
        result = set()
        for j in range(3, len(text) + 1):
            for i in range(0, j):
                if j - i & 1 > 0:
                    continue
                if self.check(text[i:j]):
                    result.add(text[i:j])
        return len(result)

    def check(self, text: str) -> bool:
        mid = len(text) >> 1
        return text[:mid] == text[mid:]
