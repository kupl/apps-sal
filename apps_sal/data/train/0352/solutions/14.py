from functools import lru_cache
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        d = collections.defaultdict(list)
        for w in words:
            d[len(w)].append(w)
        
        @lru_cache(None)
        def dp(w):
            if len(w) == 1:
                return 1
            for candidate in d[len(w) - 1]:
                for i in range(len(w)):
                    if candidate == w[:i] + w[i+1:]:
                        return dp(candidate) + 1
            return 1
        
        return max(dp(i) for i in words)

