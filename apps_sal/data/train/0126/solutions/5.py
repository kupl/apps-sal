import collections


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        def T(): return collections.defaultdict(T)
        trie, res = T(), 0
        data = [[trie, set()] for _ in range(len(s) - minSize + 1)]
        for i in range(minSize):
            for j in range(len(s) - minSize + 1):
                c = s[i + j]
                cur = data[j]
                cur[1].add(c)
                if i == minSize - 1 and len(cur[1]) <= maxLetters:
                    cur[0][c].setdefault('
                    cur[0][c]['
                    res=max(res, cur[0][c]['
                cur[0]=cur[0][c]
        return res
