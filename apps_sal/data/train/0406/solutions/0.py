class Solution:

    def ladderLength(self, beginWord, endWord, wordList):
        wordDict = set(wordList)
        if not endWord in wordDict:
            return 0
        visited = set()
        beginSet = set()
        beginSet.add(beginWord)
        visited.add(beginWord)
        endSet = set()
        endSet.add(endWord)
        visited.add(endWord)
        lenWord = len(beginWord)
        distance = 1
        while len(beginSet) > 0 and len(endSet) > 0:
            if len(beginSet) > len(endSet):
                (beginSet, endSet) = (endSet, beginSet)
            newSet = set()
            for w in beginSet:
                for i in range(lenWord):
                    part1 = w[:i]
                    part2 = w[i + 1:]
                    for alpha in 'abcdefghijklmnopqrstuvwxyz':
                        target = part1 + alpha + part2
                        if target in endSet:
                            return distance + 1
                        elif not target in visited and target in wordDict:
                            newSet.add(target)
                            visited.add(target)
            beginSet = newSet
            distance += 1
        return 0
