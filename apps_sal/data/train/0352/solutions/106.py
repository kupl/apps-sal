class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0

        words = sorted(words, key=len)

        DP = [1 for idx in range(len(words))]

        for i in range(len(words)):

            for j in range(0, i):
                if len(words[i]) == len(words[j]) + 1:

                    diff = 0

                    for comp in range(len(words[i])):

                        if diff == 0 and comp == len(words[i]) - 1:
                            diff = 1

                        elif words[i][comp] != words[j][comp - diff]:
                            if diff == 1:
                                diff = None
                                break
                            else:
                                diff = 1

                    if diff == 1:
                        if DP[j] + 1 > DP[i]:
                            DP[i] = DP[j] + 1

        return max(DP)
