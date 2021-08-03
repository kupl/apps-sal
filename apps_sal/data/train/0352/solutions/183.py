class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        words.sort(key=len)
        print(words)
        solutions = []

        numWords = len(words)

        for i in range(numWords):
            self.getSequences(words[i + 1:], len(words[i]) + 1, [words[i]], words[i], solutions)

        maxSize = 0

        for s in solutions:
            maxSize = max(maxSize, len(s))

        return maxSize

    def getSequences(self, words, targetLength, currSequence, lastWord, solutions):

        numWords = len(words)
        for i in range(numWords):
            if len(words[i]) == targetLength:
                if self.isPredecessor(lastWord, words[i]):
                    newCurrSequence = currSequence[:]
                    newCurrSequence.append(words[i])
                    self.getSequences(words[i + 1:], targetLength + 1, newCurrSequence, words[i], solutions)

            elif len(words[i]) > targetLength:
                break

        if len(solutions) > 0:
            if len(solutions[0]) < len(currSequence):
                solutions[0] = currSequence
        else:
            solutions.append(currSequence)
        return

    def isPredecessor(self, word1, word2):

        numLetters1 = len(word1)
        numLetters2 = len(word2)

        if numLetters2 - numLetters1 != 1:
            return False

        p1 = 0
        p2 = 0
        count = 0

        while p1 < numLetters1:
            if word1[p1] == word2[p2]:
                p1 += 1
                p2 += 1
            elif count == 1:
                return False
            else:
                count += 1
                p2 += 1

        return True
