class Solution:

    def distinctEchoSubstrings(self, text: str) -> int:
        (n, size, res) = (len(text), 1, set())
        while size * 2 <= n:
            count = 0
            for i in range(size):
                if text[i] == text[i + size]:
                    count += 1
            for j in range(n - 2 * size + 1):
                if count == size:
                    res.add(text[j:j + 2 * size])
                if text[j] == text[j + size]:
                    count -= 1
                if j + 2 * size < n and text[j + size] == text[j + 2 * size]:
                    count += 1
            size += 1
        return len(res)
