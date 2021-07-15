class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        longestchain = defaultdict(int)
        for word in sorted(words, key=len):
            for i in range(len(word)):
                longestchain[word] = max(longestchain[word[:i] + word[i+1:]] + 1, longestchain[word])
        return max(longestchain.values()) 

