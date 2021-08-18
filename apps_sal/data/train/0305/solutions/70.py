class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:

        if len(set(text)) == 1:
            return len(text) // 2

        rabin = [0]
        for char in text:
            rabin.append(rabin[-1] + ord(char))

        res = set()
        for w in range(1, (2 + len(text)) // 2):
            i = 0
            j = w
            while j <= len(text) - w:
                if rabin[j] - rabin[i] == rabin[j + w] - rabin[j]:
                    if text[i:j] == text[j:j + w]:
                        res.add(text[i:j])
                i += 1
                j += 1
        return len(res)
