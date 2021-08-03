class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        longest = 0
        word_dict = defaultdict(int)

        for word in words:
            for i in range(len(word)):
                wc = word[:i] + word[i + 1:]
                word_dict[word] = max(word_dict[wc] + 1, word_dict[word])

            longest = max(longest, word_dict[word])
        return longest
