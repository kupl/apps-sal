class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:

        L = len(text)

        count = 0
        S = set()

        for i in range(L):
            for j in range(i + 1, L):

                if j - i <= L - j:

                    # print(text[i:j])
                    # print(text[j:2*j-i])

                    if text[i:j] == text[j:2 * j - i]:
                        # print('here')

                        S.add(text[i:j])

                        # if text[i:j] not in D:
                        #    D[text[i:j]] = 1
                        #    count += 1

        return len(S)
