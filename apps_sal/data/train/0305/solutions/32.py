class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:

        L = len(text)

        count = 0
        S = set()

        for i in range(L):
            for j in range(i + 1, L):

                if j - i <= L - j:

                    if text[i:j] == text[j:2 * j - i]:

                        S.add(text[i:j])

        return len(S)
