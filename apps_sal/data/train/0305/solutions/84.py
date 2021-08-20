class Solution:

    def distinctEchoSubstrings(self, text: str) -> int:
        seen = set()
        count = 0
        for i in range(len(text) - 1):
            for j in range(i, len(text), 1):
                l = (j - i + 1) // 2
                if l < 1:
                    continue
                h = l + i
                t = text[i:h + l]
                if t in seen:
                    continue
                if t[:l] == t[l:]:
                    count += 1
                    seen.add(t)
        return count
