from itertools import permutations


class Solution:
    digitMap = {}
    wordsRev = []
    resultRev = []
    limit = 0

    def findSolution(self, n, carry=0):
        if n == self.limit:
            # Check leading zero policy
            leadingDigitChars = [w[len(w) - 1] for w in self.wordsRev]
            leadingDigitChars.append(self.resultRev[len(self.resultRev) - 1])
            leadingDigits = [self.digitMap[c] for c in leadingDigitChars]
            return 0 not in leadingDigits

        availableDigits = [n for n in range(0, 10) if n not in self.digitMap.values()]
        digitChars = [w[n] for w in self.wordsRev if n < len(w)]
        resultChar = self.resultRev[n]

        knownDigitChars = list(filter(lambda x: x in self.digitMap, digitChars))
        unknownDigitChars = [w for w in digitChars if w not in knownDigitChars]

        digits = []
        resultDigit = -1
        if len(knownDigitChars) > 0:
            digits = [self.digitMap[k] for k in knownDigitChars]
        if resultChar in self.digitMap:
            resultDigit = self.digitMap[resultChar]

        for d in permutations(availableDigits, len(unknownDigitChars)):
            s = sum(digits) + sum(d) + carry
            c = int(s / 10)
            s %= 10

            if resultDigit >= 0 and s == resultDigit:
                for i, v in enumerate(d):
                    self.digitMap[unknownDigitChars[i]] = v
                if self.findSolution(n + 1, c):
                    return True
                else:
                    # Fallback
                    for i, v in enumerate(d):
                        if unknownDigitChars[i] in self.digitMap:
                            del self.digitMap[unknownDigitChars[i]]
            elif resultDigit < 0 and ((resultChar not in unknownDigitChars and s not in d) or (resultChar in unknownDigitChars and s in d)) and s in availableDigits:
                for i, v in enumerate(d):
                    self.digitMap[unknownDigitChars[i]] = v
                if resultChar not in unknownDigitChars:
                    self.digitMap[resultChar] = s
                elif s != self.digitMap[resultChar]:
                    for i, v in enumerate(d):
                        if unknownDigitChars[i] in self.digitMap:
                            del self.digitMap[unknownDigitChars[i]]
                    continue

                if self.findSolution(n + 1, c):
                    return True
                else:
                    # Fallback
                    for i, v in enumerate(d):
                        if unknownDigitChars[i] in self.digitMap:
                            del self.digitMap[unknownDigitChars[i]]
                    if resultChar in self.digitMap:
                        del self.digitMap[resultChar]
        return False

    def isSolvable(self, words: List[str], result: str) -> bool:
        self.digitMap = {}
        self.wordsRev = [w[::-1] for w in words]
        self.resultRev = result[::-1]

        wordMax = max([len(w) for w in words])
        if wordMax > len(result):
            return False

        self.limit = max(wordMax, len(result))

        return self.findSolution(0, 0)
