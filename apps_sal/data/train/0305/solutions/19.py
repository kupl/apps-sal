class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        ansSet = set()
        for i in range(len(text)):
            for j in range(i + 1, (i + 1 + len(text) + 1) // 2):
                if text[i: j] == text[j: 2 * j - i]:
                    ansSet.add(text[i: 2 * j - i])
        return len(ansSet)
