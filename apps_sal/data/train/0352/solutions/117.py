class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        word_list = sorted(words, key=lambda x: len(x))
        word_dict = {word: 1 for word in word_list}
        longest = 0
        for word in word_list:
            for i in range(len(word)):
                test = word[:i] + word[i + 1:]
                if test in word_dict:
                    word_dict[word] = word_dict[test] + 1
                longest = max(longest, word_dict[word])
        return longest
