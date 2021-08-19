class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # sort by decreasing length
        # define vector L of length len(words) such that it's the longest
        # word chain starting from that word
        # then recuriosn is L_k = 1 if it is not predecessor of any 1 longer words
        # otherwise it is 1 + max L_j for j such that k is predecessor of them

        lengths = [len(word) for word in words]
        wordsSorted = [x for _, x in sorted(zip(lengths, words), reverse=True)]

        print(wordsSorted)
        L = [1] * len(wordsSorted)
        maxLength = max(lengths)
        for k in range(0, len(L)):
            lenWord = len(wordsSorted[k])
            for l in range(k):
                if len(wordsSorted[l]) == lenWord + 1 and (set(wordsSorted[l]) & set(wordsSorted[k])) == set(wordsSorted[k]):
                    L[k] = max(L[k], 1 + L[l])
        return(max(L))
