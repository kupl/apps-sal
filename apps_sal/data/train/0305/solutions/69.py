class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:

        subs = set()

        for i in range(len(text)):
            for j in range(i + 1, len(text)):

                temp = text[i:j]

                # print(\"\\t\\t temp:\",temp,\"\\t\\t \",temp==text.startswith(temp,j))
                if text[i:j] == text[j:j + j - i]:  # text.startswith(text[i:j],j):
                    subs.add(text[i:j])

        # print(subs)
        return len(subs)
