class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wc = {}
        for w in words:
            wc.setdefault(len(w), [])
            wc[len(w)].append(w)
        
        d = {}
        for i in sorted(wc.keys()):
            if i - 1 not in wc:
                for w in wc[i]:
                    d[w] = 1
            else:
                for w in wc[i]:
                    d[w] = 1
                    for i in range(len(w)):
                        if w[:i] + w[i+1:] in d:
                            d[w] = max(d[w], d[w[:i] + w[i+1:]] + 1)
        return max(d.values())
