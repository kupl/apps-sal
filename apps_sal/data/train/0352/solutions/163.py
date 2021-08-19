class Solution:

    def isPredecessor(self, predecessorCandidate, word):
        if len(predecessorCandidate) != len(word) - 1:
            return False
        pWhere = 0
        wWhere = 0
        hasSkipped = False
        while pWhere < len(predecessorCandidate) and wWhere < len(word):
            if predecessorCandidate[pWhere] != word[wWhere]:
                if hasSkipped:
                    return False
                hasSkipped = True
                wWhere += 1
            else:
                wWhere += 1
                pWhere += 1
        return True

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        predecessorDict = collections.defaultdict(list)
        chainCountDict = collections.defaultdict(lambda: 1)
        currentMax = 1
        for i in range(0, len(words)):
            for j in range(i + 1, len(words)):
                if self.isPredecessor(words[i], words[j]):
                    predecessorDict[words[j]].append(words[i])
                    chainCountDict[words[j]] = max(chainCountDict[words[j]], 1 + chainCountDict[words[i]])
                    currentMax = max(currentMax, chainCountDict[words[j]])
        return currentMax
