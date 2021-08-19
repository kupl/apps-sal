from collections import defaultdict, deque


class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        words_set = set(words)

        def helper(word):
            if len(word) == 0:
                return 0
            for index in range(len(word)):
                string = word[:index] + word[index + 1:]
                if string not in maxChain and string in words_set:
                    helper(string)
                maxChain[word] = max(maxChain[word], maxChain[string] + 1)
            return maxChain[word]
        maxChain = defaultdict(lambda: 0)
        for word in words:
            maxVal = 0
            if word not in maxChain:
                helper(word)
        return max(maxChain.values())
