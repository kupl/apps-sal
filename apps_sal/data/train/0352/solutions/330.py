class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordSet = set(words)
        i_min = min(wordSet)
        @lru_cache()
        def aux(word):
            if not word or word not in wordSet: return 0
            if len(word) == i_min: return 1
            return 1+max(aux(word[:i]+word[i+1:]) for i in range(len(word)))
        return max(aux(w) for w in words)
