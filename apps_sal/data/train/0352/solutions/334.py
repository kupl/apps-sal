class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        from collections import defaultdict
        words.sort(key=lambda word:len(word), reverse=True)
        length = defaultdict(int)
        longest = 0
        for word in words:
            length[word] = max(length[word], 1)
            longest = max(longest, length[word])
            for i in range(len(word)):
                length[word[:i] + word[i+1:]] = max(length[word[:i] + word[i+1:]], length[word] + 1)
        return longest
