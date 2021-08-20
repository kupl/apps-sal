from functools import lru_cache


class Solution:

    def longestStrChain(self, words: List[str]) -> int:

        @lru_cache
        def chain_len(word):
            return 1 + max((chain_len(word[:i] + word[i + 1:]) for i in range(len(word)))) if word in valid else 0
        valid = set(words)
        return max((chain_len(word) for word in words))
