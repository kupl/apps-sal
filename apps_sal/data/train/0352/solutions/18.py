class Solution:

    def longestStrChain(self, words: List[str]) -> int:

        def longest_chain(word, word_set, memo):
            if word not in word_set:
                return 0
            if word not in memo:
                longest = 1
                for i in range(len(word)):
                    next_word = word[:i] + word[i + 1:]
                    longest = max(1 + longest_chain(next_word, word_set, memo), longest)
                memo[word] = longest
            return memo[word]
        longest = 0
        for word in words:
            longest = max(longest_chain(word, set(words), {}), longest)
        return longest
