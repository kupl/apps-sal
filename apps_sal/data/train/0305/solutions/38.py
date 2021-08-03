class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        result = set()
        size = len(text)
        for i in range(size):
            for j in range(i + 1, size):
                if text[i:j] == text[j:j + (j - i)]:
                    result.add(text[i:j])

        return len(result)
