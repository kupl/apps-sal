# DFS | Time: O(n * k) | Space: O(n)
# n: len(words)
# k: length of each word
class Solution:

    # @param words: List[str]
    # @return int
    def longestStrChain(self, words):
        if not words:
            return 0

        # build word table
        wordTable = self.buildWordTable(words)  # { length: list of words }

        # dfs - search from shortest word to longest word
        maxLen = 0
        visited = set()
        for wordLen in range(min(wordTable), max(wordTable) + 1):
            for word in wordTable[wordLen]:
                if word not in visited:
                    maxLen = max(maxLen, self.dfs(wordTable, word, visited))

        return maxLen

    # Derive word table.
    # Key: word length.
    # Value: list of words that have length of key.
    # @param words: List[str]
    # @return dict({ int: List[str] })
    def buildWordTable(self, words):

        # initialize
        wordTable = {}  # { length: list of words }

        for word in words:
            if len(word) not in wordTable:
                wordTable[len(word)] = []
            wordTable[len(word)].append(word)

        return wordTable

    # DFS - search the successors and find the longest chain
    #   - Apply Divide & Conquer coding framework
    # @param wordTable: dict({ int: List[str] })
    # @param word: str
    # @param visited: set(str)
    # @return int
    def dfs(self, wordTable, word, visited):

        # initialize
        maxLen = 0
        visited.add(word)

        # divide
        #   - Find successors and update the max length that subtasks responded
        if len(word) + 1 in wordTable:
            for neighbor in wordTable[len(word) + 1]:
                if self.isAncestor(word, neighbor):
                    maxLen = max(maxLen, self.dfs(wordTable, neighbor, visited))

        # conquer
        #   - Calculate the max length found
        #   - +1 to count itself
        return maxLen + 1

    # @param ancestor: str
    # @param successor: str
    # @return bool
    def isAncestor(self, ancestor, successor):
        if len(ancestor) + 1 != len(successor):
            return False

        # initialize
        i, j = 0, 0

        while i < len(ancestor) and j < len(successor):
            if ancestor[i] != successor[j]:
                j += 1
                continue
            else:
                i += 1
                j += 1

        return i == j or i == j - 1
