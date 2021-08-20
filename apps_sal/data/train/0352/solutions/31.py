class Solution:

    def longestStrChain(self, words: List[str]) -> int:

        def check(i, j):
            w1 = words[i]
            w2 = words[j]
            for k in range(len(w2)):
                if w1 == w2[:k] + w2[k + 1:]:
                    return True
            return False
        buckets = defaultdict(list)
        for (i, word) in enumerate(words):
            l = len(word)
            buckets[l] += [i]
        g = defaultdict(list)
        for key in buckets:
            if key + 1 in buckets:
                for i in buckets[key]:
                    for j in buckets[key + 1]:
                        if check(i, j):
                            g[i] += [j]
        ans = 0
        seen = set()
        for key in sorted(buckets.keys()):
            for i in buckets[key]:
                stack = [[1, i]]
                while stack:
                    (level, node) = stack.pop()
                    ans = max(ans, level)
                    if node in seen:
                        continue
                    seen.add(node)
                    if node in g:
                        for child in g[node]:
                            if child not in seen:
                                stack += [[level + 1, child]]
        return ans
