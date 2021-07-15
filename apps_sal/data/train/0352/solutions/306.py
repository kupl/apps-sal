class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        cache = {}
        words_dict = {word:None for word in words}
        def chain(word):
            if word in cache: return cache[word]
            if word in words:
                cache[word] = 1 + max(
                    map(chain, [word[:idx]+word[idx+1:] for idx in range(len(word))])
                )
                return cache[word]
            return 0
        return max(map(chain, words))
