class Solution:

    def distinctEchoSubstrings(self, text: str) -> int:
        N = len(text)
        s = set()
        for offset in range(1, N // 2 + 1):
            K = 0
            for j in range(N - offset):
                if text[j] == text[j + offset]:
                    K += 1
                else:
                    K = 0
                if K >= offset:
                    s.add(text[j - offset + 1:j + offset + 1])
        return len(s)
