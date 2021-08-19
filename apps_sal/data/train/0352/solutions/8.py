class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        all_chains = []
        for word in words:
            all_chains.extend(self.createChains(word, words))
        return max(map(len, all_chains))

    def createChains(self, word, words):
        result = []
        step = [word]
        dictionary = set(words)
        self.helper(word, step, dictionary, result)
        return result

    def helper(self, word, step, dictionary, result):
        result.append(step[:])
        for i in range(len(word) - 1, -1, -1):
            substring = word[:i] + word[i + 1:]
            if substring in dictionary:
                step.append(substring)
                self.helper(substring, step, dictionary, result)
                step.pop()
