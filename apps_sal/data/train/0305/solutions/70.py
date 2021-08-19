class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:

        # 1. Use two pointers, start with 2 pointers that are 1 space apart
        # 2. Then space the pointers 2, 3, 4 up to len(text)//2
        # 3. Run the pointers along the text and anytime text[i] == text[j]
        #    expand until i reaches where j started or text[i] != text[j]
        #
        #    Optimization, rabin-karp hash the entire text and check if len(i+window)-i == len(j+window) - j

        if len(set(text)) == 1:
            return len(text) // 2

        rabin = [0]
        for char in text:
            rabin.append(rabin[-1] + ord(char))

        # print(rabin)
        res = set()
        for w in range(1, (2 + len(text)) // 2):
            i = 0
            j = w
            while j <= len(text) - w:
                if rabin[j] - rabin[i] == rabin[j + w] - rabin[j]:
                    #print(text[i:j], rabin[j] - rabin[i], rabin[j+w] - rabin[j])
                    if text[i:j] == text[j:j + w]:
                        res.add(text[i:j])
                i += 1
                j += 1
        return len(res)
