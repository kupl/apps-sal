class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        ans = 0
        visited = set()
        textLen = len(text)
        for i in range(textLen - 1):
            for j in range(0, min(i + 1, textLen - i - 1)):
                if text[i - j:i + 1] == text[i + 1:i + j + 2]:
                    if text[i - j:i + 1] not in visited:
                        visited.add(text[i - j:i + 1])
                        ans += 1
        return ans
