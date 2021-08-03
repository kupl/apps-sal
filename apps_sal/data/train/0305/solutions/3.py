class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:

        seen = set()

        count = 0

        for i in range(len(text) - 1):
            for j in range(i, len(text), 1):
                # h = j//2
                # l = h - i

                l = (j - i + 1) // 2
                h = l + i

                # print(text[i:h], text[h:h+l], i, j)
                if l < 1 or text[i:h + l] in seen:
                    continue

                if text[i:h] == text[h:h + l]:
                    count += 1
                    # print( '**', text[i:h+l])
                    seen.add(text[i:h + l])

        return count


#     2 7

#     l=(j-i+1)//2
#     h=l//2


#     0 8

#     0:4 4:4+(8-0)//2
