from functools import lru_cache

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        @lru_cache
        def chain_len(w):
            return 1 + max(chain_len(w[:i] + w[i+1:]) for i in range(len(w))) if w in valid else 0
        
        valid = set(words)
        return max(chain_len(w) for w in words)
