class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        longestchain = defaultdict(int)
        words.sort(key=len, reverse=True)
        for word in words:
            for i in range(len(word)):
                pred = word[:i] + word[i + 1:]
                longestchain[pred] = max(longestchain[pred], 1 + longestchain[word])
        return max(longestchain.values())
