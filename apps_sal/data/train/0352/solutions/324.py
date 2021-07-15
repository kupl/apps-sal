class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = set(words)
        @lru_cache()
        def helper(word):
            if not word or word not in words: 
                return 0
            return 1 + max(helper(word[:i] + word[i + 1:]) for i in range(len(word)))
        return max(helper(word) for word in words)
