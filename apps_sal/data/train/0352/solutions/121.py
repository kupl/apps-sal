class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def connected(x, y):
            i, j = 0, 0
            count = 0
            while i < len(y) and j < len(x):
                if y[i] != x[j]:
                    if count == 0:
                        j += 1
                        count += 1
                    else:
                        return False
                else:
                    i += 1
                    j += 1
            return True

        sort_words = sorted(words, key=len)
        res = [1 for i in range(len(sort_words))]

        for i in range(len(sort_words)):
            x = sort_words[i]
            for j in range(i, len(sort_words)):
                y = sort_words[j]
                if len(y) == len(x) + 1 and connected(y, x):
                    res[j] = max(res[j], res[i] + 1)
                elif len(y) > len(x) + 1:
                    break
        return max(res)
