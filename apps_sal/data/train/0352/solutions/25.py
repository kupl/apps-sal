class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        lengths = [len(word) for word in words]
        wordsSorted = [x for _, x in sorted(zip(lengths, words), reverse=True)]

        print(wordsSorted)
        L = [1] * len(wordsSorted)
        maxLength = max(lengths)
        for k in range(0, len(L)):
            lenWord = len(wordsSorted[k])
            if lenWord == maxLength:
                L[k] = 1
            else:
                for l in range(k):
                    if len(wordsSorted[l]) == lenWord + 1 and (set(wordsSorted[l]) & set(wordsSorted[k])) == set(wordsSorted[k]):
                        L[k] = max(L[k], 1 + L[l])
        return(max(L))
