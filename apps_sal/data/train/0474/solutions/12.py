from collections import Counter


class Solution:
    def subsets(self, words: List[str]) -> List[List[str]]:
        def subsetsHelper(words: List[str]) -> List[List[str]]:
            if len(words) == 0:
                return [[]]
            result = subsetsHelper(words[1:])
            for i in range(len(result)):
                if result[i] != None:
                    l = result[i][:]
                    l.append(words[0])
                    result.append(l)
            return result
        return subsetsHelper(words)

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def getScores(wordSet: List[str]) -> int:
            scoreCount = 0
            counter = Counter(letters)
            for word in wordSet:
                for c in word:
                    if not c in counter or counter[c] == 0:
                        return 0
                    counter[c] -= 1
                    scoreCount += score[ord(c) - ord('a')]
            return scoreCount

        ans = 0
        for wordSet in self.subsets(words):
            currentScore = getScores(wordSet)
            if currentScore > ans:
                ans = currentScore
        return ans
