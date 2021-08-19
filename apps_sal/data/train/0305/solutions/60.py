class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        subs = set()

        for i in range(len(text)):
            for j in range(i + 1, len(text)):

                temp = text[i:j]
                if text[i:j] == text[j:j + j - i]:
                    subs.add(text[i:j])

    # print(subs)
        return len(subs)
