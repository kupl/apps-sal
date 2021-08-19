class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        chain = {}
        for w in sorted(words, key=len):
            weights = [chain.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w))]
            chain[w] = max(weights)
        return max(chain.values())
