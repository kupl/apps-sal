class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        from collections import defaultdict
        d = {}
        for word in words:
            if len(word) in d:
                d[len(word)].append(word)
            else:
                d[len(word)] = [word]

        def isPred(w1, w2):
            for i in range(len(w2)):
                if w2[:i] + w2[i + 1:] == w1:
                    return True
            return False
        followers = defaultdict(list)
        for word in words:
            if len(word) + 1 in d:
                for biggerWord in d[len(word) + 1]:
                    if isPred(word, biggerWord):
                        followers[word].append(biggerWord)
        self.maxDist = 1

        def dfs(start, dist, found=set()):
            found.add(start)
            for neighbor in followers[start]:
                if neighbor not in found:
                    self.maxDist = max(self.maxDist, dist + 1)
                    dfs(neighbor, dist + 1, found)
        keys = [key for key in followers]
        for key in keys:
            s = set()
            dfs(key, 1, set())
        return self.maxDist
