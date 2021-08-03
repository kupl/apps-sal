class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = list(set(words))
        words = sorted(words, key=lambda x: len(x))

        # key is current word, value is current length
        chains = {}
        len_arr = [len(x) for x in words]
        min_len, max_len = min(len_arr), max(len_arr)
        max_len_w = [w for w in words if len(w) == max_len]
        for w in max_len_w:
            chains[w] = 1

        for length in range(max_len - 1, min_len - 1, -1):
            for w in words:
                if len(w) != length:
                    continue
                max_w = 1
                for key in chains:
                    if len(key) == len(w) + 1 and self.is_chain(w, key):
                        max_w = max(max_w, chains[key] + 1)
                chains[w] = max_w

        len_chain = [y for x, y in list(chains.items())]
        return max(len_chain)

    def is_chain(self, small_w, large_w):
        for i in range(len(large_w)):
            if large_w[:i] + large_w[i + 1:] == small_w:
                return True
        return False
