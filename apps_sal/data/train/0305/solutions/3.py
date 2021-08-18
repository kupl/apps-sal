class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:

        seen = set()

        count = 0

        for i in range(len(text) - 1):
            for j in range(i, len(text), 1):

                l = (j - i + 1) // 2
                h = l + i

                if l < 1 or text[i:h + l] in seen:
                    continue

                if text[i:h] == text[h:h + l]:
                    count += 1
                    seen.add(text[i:h + l])

        return count
