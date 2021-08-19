class Solution:

    def predecessor(self, larger, smaller):
        largerCount = Counter(larger)
        for c in smaller:
            if c in largerCount:
                largerCount[c] -= 1
                if largerCount[c] == 0:
                    del largerCount[c]
        mc = largerCount.most_common()
        return len(mc) == 1 and mc[0][1] == 1

    def longestStrChain(self, words: List[str]) -> int:
        lengthToWords = defaultdict(list)
        for word in words:
            lengthToWords[len(word)].append(word)
        wordToCL = defaultdict(lambda: 1)
        res = 1
        for wordLength in range(16, 1, -1):
            if wordLength - 1 not in lengthToWords:
                continue
            for larger in lengthToWords[wordLength]:
                for smaller in lengthToWords[wordLength - 1]:
                    if self.predecessor(larger, smaller):
                        wordToCL[smaller] = max(wordToCL[smaller], wordToCL[larger] + 1)
                        res = max(res, wordToCL[smaller])
        return res
