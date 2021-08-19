class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        preToPost = collections.defaultdict(set)
        for word1 in words:
            for word2 in words:
                if self.isPredecessor(word1, word2):
                    preToPost[word1].add(word2)
        ans = 0
        memo = {}
        for word in words:
            ans = max(ans, self.dfs(word, preToPost, memo))
        return ans

    def dfs(self, word, preToPost, memo):
        if word in memo:
            return memo[word]
        ans = 1
        for post in preToPost[word]:
            ans = max(ans, 1 + self.dfs(post, preToPost, memo))
        memo[word] = ans
        return memo[word]

    def isPredecessor(self, word1, word2):
        if not len(word1) + 1 == len(word2):
            return False
        missed = False
        i = 0
        j = 0
        while i < len(word1) and j < len(word2) and (word1[i] == word2[j]):
            i += 1
            j += 1
        j += 1
        while i < len(word1) and j < len(word2) and (word1[i] == word2[j]):
            i += 1
            j += 1
        return i == len(word1) and j == len(word2)
