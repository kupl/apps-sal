class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        size = 0
        wordSet = set(words)
        mem = {}

        def dfs(s):
            if s in mem:
                return mem[s]
            maxpath = 1
            for i in range(len(s)):
                new = s[:i] + s[i + 1:]
                if new in wordSet:
                    maxpath = max(maxpath, 1 + dfs(new))
            mem[s] = maxpath
            return mem[s]
        for word in words:
            if word not in mem:
                size = max(size, dfs(word))
        print(mem)
        return size
        dic = collections.defaultdict(int)
        words = sorted(words, key=lambda x: len(x))
        for word in words:
            dic[word] = 1
            for i in range(len(word)):
                tmp = word[:i] + word[i + 1:]
                if tmp in dic:
                    dic[word] = max(dic[word], dic[tmp] + 1)
        return max(dic.values())
