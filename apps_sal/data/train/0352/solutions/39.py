class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        self._len_to_words = collections.defaultdict(list)
        for w in words:
            self._len_to_words[len(w)].append(w)
        if len(self._len_to_words) == 1:
            return 1
        self._cache = {}
            
        self._visited = {}
        max_so_far = 0
        for w in words:
            max_so_far = max(max_so_far, self._find_longest(w))
        return max_so_far
    
    def _find_longest(self, w):
        if w in self._visited:
            return self._visited[w]
        
        len_w = len(w)
        if len_w+1 not in self._len_to_words:
            self._visited[w] = 1
            return 1
        
        max_chain_len = 1
        for cand in self._len_to_words[len_w+1]:
            if self.is_predecessor(w, cand):
                max_chain_len = max(max_chain_len, 1+self._find_longest(cand))
        
        self._visited[w] = max_chain_len
        return max_chain_len
        
    def is_predecessor(self, w1, w2):
        if (w1, w2) in self._cache:
            return self._cache[(w1, w2)]
        
        is_p = True
        if len(w1) + 1 != len(w2):
            is_p = False
        else:
            count = {}
            for c in w1:
                if c in count:
                    count[c] += 1
                else:
                    count[c] = 1
            found_diff = False
            for c in w2:
                if c in count:
                    count[c] -= 1
                    if count[c] == 0:
                        del count[c]
                else:
                    if found_diff:
                        is_p = False
                        break
                    else:
                        found_diff = True
                        count[c] = 1
        if is_p:
            keys = list(count.keys())
            is_p = len(keys) == 1 and count[keys[0]] == 1
        
        self._cache[(w1, w2)] = is_p
        return is_p
