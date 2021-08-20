class Solution:

    def distinctEchoSubstrings(self, text: str) -> int:
        count = 0
        visited = {}
        for i in range(len(text)):
            for length in range(1, len(text) // 2 + 1):
                now = text[i:i + length]
                if now in visited:
                    continue
                if now == text[i + length:i + 2 * length]:
                    count += 1
                    visited[now] = 1
        return count
