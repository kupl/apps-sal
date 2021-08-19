class Solution:

    def longestStrChain(self, words):
        if not words:
            return 0
        wordTable = self.buildWordTable(words)
        maxLen = 0
        visited = set()
        for wordLen in range(min(wordTable), max(wordTable) + 1):
            for word in wordTable[wordLen]:
                if word not in visited:
                    maxLen = max(maxLen, self.dfs(wordTable, word, visited))
        return maxLen

    def buildWordTable(self, words):
        wordTable = {}
        for word in words:
            if len(word) not in wordTable:
                wordTable[len(word)] = []
            wordTable[len(word)].append(word)
        return wordTable

    def dfs(self, wordTable, word, visited):
        maxLen = 0
        visited.add(word)
        if len(word) + 1 in wordTable:
            for neighbor in wordTable[len(word) + 1]:
                if self.isAncestor(word, neighbor):
                    maxLen = max(maxLen, self.dfs(wordTable, neighbor, visited))
        return maxLen + 1

    def isAncestor(self, ancestor, successor):
        if len(ancestor) + 1 != len(successor):
            return False
        (i, j) = (0, 0)
        while i < len(ancestor) and j < len(successor):
            if ancestor[i] != successor[j]:
                j += 1
                continue
            else:
                i += 1
                j += 1
        return i == j or i == j - 1
