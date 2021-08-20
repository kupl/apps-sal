class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        dic = defaultdict(list)
        words.sort(key=len, reverse=True)
        for w in words:
            for i in range(len(w)):
                if w[:i] + w[i + 1:] in words:
                    dic[w].append(w[:i] + w[i + 1:])

        def bt(x):
            return [[x]] if x not in dic else [[x] + rest for y in dic[x] for rest in bt(y)]
        ct = 1
        for word in words:
            ct = max(ct, len(max(bt(word), key=len)))
        return ct
