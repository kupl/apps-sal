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

                # print(text[i:h], text[h:h+l], i, j)
                if t in seen:
                    continue

                if t[:l] == t[l:]:
                    count += 1
                    # print( '**', text[i:h+l])
                    seen.add(t)

        return count
